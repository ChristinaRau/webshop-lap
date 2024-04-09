
import { sendRequest } from "../Request";
import { camelToSnakeCase } from "../StringUtils";

export class Addition {
    id?: number;
    name: string;
    value: string;
    price: number;
    static path = "addition";

    constructor(name: string, value: string, price: number, id: number) {
        this.name = name;
        this.value = value;
        this.price = price;
        this.id = id;
    }

    public static mandatoryAttributes = ["name", "value", "price"]

    public static checkMandatoryAttributes(obj: Record<string, any>) {
        return this.mandatoryAttributes.every((el) => Object.keys(obj).includes(el))
    }

    public toSnakeCaseObject() {
        const newObject = <Record<string, any>>{}
        for (const key in this) {
            newObject[camelToSnakeCase(key)] = this[key]
        }

        return newObject;
    }

    public static fromSnakeCaseObject(snakeCaseObj: Record<string, any>) {
        // check if every needed attribute is in the snake case object
        if (this.checkMandatoryAttributes(snakeCaseObj))
            return new Addition(
                snakeCaseObj.name,
                snakeCaseObj.value,
                snakeCaseObj.price,
                snakeCaseObj.id
                )
        return new Addition("", "", 0, -1);
    }

    // static async loadById(id: number) {
    //     return await this.get(id).then((response) => {
    //         return response
    //     })
    // }


    static async getList(): Promise<Addition[]> {
        const jsonResponse: Record<string, any> | Array<Record<string, any>> = await sendRequest({
            method: "GET",
            path: this.path
        }).then((resp) => {
            return resp.json()
        }).then((resp) => {
            return resp;
        });

        return jsonResponse.map((obj: Record<string, any>) => this.fromSnakeCaseObject(obj))
    }

    static async get(id: number): Promise<Addition> {
        const jsonResponse: Record<string, any> | Array<Record<string, any>> = await sendRequest({
            id:  id,
            method: "GET",
            path: this.path
        }).then((resp) => {
            return resp.json()
        }).then((resp) => {
            return resp;
        });

        return this.fromSnakeCaseObject(jsonResponse)
    }

    create() {
        return sendRequest({
            method: "POST",
            path: Addition.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        })
    }

    update() {
        return sendRequest({
            id: this.id,
            method: "PATCH",
            path: Addition.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        })
    }

    delete() {
        return sendRequest({
            id: this.id,
            method: "DELETE",
            path: Addition.path
        })
    }


}