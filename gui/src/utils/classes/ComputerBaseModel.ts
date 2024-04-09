
import { sendRequest } from "../Request";
import { camelToSnakeCase } from "../StringUtils";

// *name: varchar
// *ram_gigabyte: float 
// *price: float
// *storage_gigabyte: float
// *processor: string
// image_path: string
// description: varchar

export class ComputerBaseModel {
    id?: number;
    name: string;
    ramGigabyte: number;
    price: number;
    storageGigabyte: number;
    processor: string;
    imagePath?: string;
    description?: string;

    static path = "computer-base-model";

    constructor(name: string,
        ramGigabyte: number,
        price: number,
        storageGigabyte: number,
        processor: string,
        imagePath?: string,
        description?: string,
        id?: number
    ) {
        this.name = name;
        this.ramGigabyte = ramGigabyte;
        this.price = price;
        this.storageGigabyte = storageGigabyte;
        this.processor = processor;
        this.imagePath = imagePath;
        this.description = description;
        this.id = id; 
    }

    public static mandatoryAttributes = [
        "name",
        "ram_gigabyte",
        "price",
        "storage_gigabyte",
        "processor"
    ];

    public static checkMandatoryAttributes(obj: Record<string, any>) {
        return this.mandatoryAttributes.every((el) => Object.keys(obj).includes(el));
    }

    public isValid() {
        return (
            this.name !== undefined && this.name.length > 0 &&
            this.processor !== undefined && this.name.length > 0 &&
            this.price !== undefined &&
            this.ramGigabyte !== undefined &&
            this.storageGigabyte !== undefined
        );
    }

    public toSnakeCaseObject() {
        const newObject = <Record<string, any>>{};
        for (const key in this) {
            newObject[camelToSnakeCase(key)] = this[key];
        }

        return newObject;
    }

    public static fromSnakeCaseObject(snakeCaseObj: Record<string, any>) {
        // check if every needed attribute is in the snake case object
        if (this.checkMandatoryAttributes(snakeCaseObj))
            return new ComputerBaseModel(
                snakeCaseObj.name,
                snakeCaseObj.ram_gigabyte,
                snakeCaseObj.price,
                snakeCaseObj.storage_gigabyte,
                snakeCaseObj.processor,
                snakeCaseObj.image_path,
                snakeCaseObj.description,
                snakeCaseObj.id
            );
        return new ComputerBaseModel("", 0, 0, 0, "");
    }

    // static async loadById(id: number) {
    //     return await this.get(id).then((response) => {
    //         return response
    //     })
    // }


    static async getList(): Promise<ComputerBaseModel[]> {
        const jsonResponse: Record<string, any> | Array<Record<string, any>> = await sendRequest({
            method: "GET",
            path: this.path
        }).then((resp) => {
            return resp.json();
        }).then((resp) => {
            return resp;
        });

        return jsonResponse.map((obj: Record<string, any>) => this.fromSnakeCaseObject(obj));
    }

    static async get(id: number): Promise<ComputerBaseModel> {
        const jsonResponse: Record<string, any> | Array<Record<string, any>> = await sendRequest({
            id:  id,
            method: "GET",
            path: this.path
        }).then((resp) => {
            return resp.json();
        }).then((resp) => {
            return resp;
        });

        return this.fromSnakeCaseObject(jsonResponse);
    }

    create() {
        return sendRequest({
            method: "POST",
            path: ComputerBaseModel.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        });
    }

    update() {
        return sendRequest({
            id: this.id,
            method: "PATCH",
            path: ComputerBaseModel.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        });
    }

    delete() {
        return sendRequest({
            id: this.id,
            method: "DELETE",
            path: ComputerBaseModel.path
        });
    }


}