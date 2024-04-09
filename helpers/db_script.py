# order = {"*id": dict(type="int", pk=True), "*reseller_id": dict(type="int", fk="reseller")}

import re
import argparse

# from api.helpers import to_snake
from collections import namedtuple

UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_snake(string):
    result = [string[0].lower()]
    for char in string[1:]:
        if char in UPPER_CASE:
            result.append("_")
        result.append(char.lower())
    return "".join(result)


def to_camel(string):
    result = [string[0].upper()]
    for index, char in enumerate(string[1:]):
        if string[index - 1] == "_":
            result.pop()
            result.append(char.upper())
        result.append(char)
    return "".join(result)


argparser = argparse.ArgumentParser()
argparser.add_argument("file", type=str)
argparser.add_argument("-m", "--add-model-files", action="store_true")
args = argparser.parse_args()

attribute = namedtuple("Attribute", ["name", "type", "constraint"])


class PlantUMLParser:
    def __init__(self, plantuml_script):
        self.plantuml_script = plantuml_script

    def parse(self):
        entity_pattern = re.compile(r"entity\s+(\w+)\s+\{([^}]*)\}", re.MULTILINE)
        attribute_pattern = re.compile(r"(\*?\w+):\s*(\w+)\s?(<<[PF]K>>)?")
        entities = entity_pattern.findall(self.plantuml_script)
        class_definitions = []
        for entity_name, attributes in entities:
            attribute_list = []
            for attribute_match in attribute_pattern.finditer(attributes):
                attribute_name, attribute_type, constraint = attribute_match.groups()
                attribute_list.append(
                    attribute(attribute_name, attribute_type, constraint)
                )
            class_definition = {
                "class_name": entity_name,
                "attributes": attribute_list,
            }
            class_definitions.append(class_definition)
        return class_definitions


class SQLAlchemyORMGenerator:
    @staticmethod
    def generate_class(class_definition):
        class_name = class_definition["class_name"]
        attributes = class_definition["attributes"]

        class_str = f"class {class_name}(Base):\n"
        class_str += "    __tablename__ = '" + to_snake(class_name) + "'\n\n"
        dict_fields = []

        for attr_name, attr_type, constraint in attributes:
            attr_name_without_star = attr_name.replace("*", "")
            attr_name_without_star = to_snake(attr_name_without_star)
            dict_fields.append(attr_name_without_star)

            class_str += f"    {attr_name_without_star}: "

            mapped_column_arguments = []

            # class_str += f"Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())"

            mapped_type = attr_type
            if mapped_type.lower().endswith("datetime"):
                mapped_type = "dt.datetime"
                mapped_column_arguments = [
                    "DateTime(timezone=True)",
                    "server_default=func.now()",
                ]

            elif mapped_type.startswith("varchar") or attr_type == "string":
                mapped_type = "str"

            if attr_name.startswith("*"):
                class_str += f"Mapped[{mapped_type}]"
            else:
                class_str += f"Mapped[Optional[{mapped_type}]]"

            if constraint is not None:
                constraint = constraint.replace("<", "").replace(">", "")

                if constraint.lower() == "pk":
                    mapped_column_arguments.append("primary_key=True")
                elif constraint.lower() == "fk":
                    mapped_column_arguments.insert(
                        0,
                        f"ForeignKey('{attr_name_without_star.replace('_id', '')}.id')",
                    )

            if len(mapped_column_arguments) > 0:
                class_str += f" = mapped_column({', '.join(mapped_column_arguments)})"

            class_str += "\n"

            dict_str = ",\n            ".join(
                f'"{field}": self.{field}' for field in dict_fields
            )

        class_str += f"""

    def to_dict(self):
        return {{
            {dict_str}
        }}
"""

        attr_names = [attr[0].replace("*", "") for attr in attributes]

        class_str += f"""

    @staticmethod
    def from_dict(dictionary) -> "{class_name}":
        class_attributes = {attr_names}
        dict_attributes = {{key : value for key, value in dictionary.items() if key in class_attributes}}

        return {class_name}(**dict_attributes)
        """

        return class_str


python_imports = """
from sqlalchemy.orm import (
	Mapped,
    mapped_column
)
from sqlalchemy import (
    ForeignKey,
    DateTime,
    func
)
from typing import Optional
import datetime as dt
from .base import Base


"""

if __name__ == "__main__":
    with open(args.file, "r") as file:
        plantuml_script = file.read()

        parser = PlantUMLParser(plantuml_script)
        class_definitions = parser.parse()

        orm_classes = []
        for class_def in class_definitions:
            generated_class = SQLAlchemyORMGenerator.generate_class(class_def)
            orm_classes.append(generated_class)

            if args.add_model_files:
                with open(
                    f"models/{to_snake(class_def['class_name'])}.py", "w"
                ) as file:
                    file.write(python_imports + generated_class)

        print(python_imports + "\n\n".join(orm_classes))
