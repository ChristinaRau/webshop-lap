
import { sendRequest } from "../Request";
import { camelToSnakeCase } from "../StringUtils";

export class ProductDetail {
    id?: number;
    productId: number;
    name: string;
    value: string;

    constructor(productId: number, name: string, value: string, id?: number) {
        this.productId = productId;
        this.name = name;
        this.value = value;
        this.id = id;
    }

    public static mandatoryAttributes = ["name", "value", "product_id"];

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
            return new ProductDetail(
                snakeCaseObj.product_id,
                snakeCaseObj.name,
                snakeCaseObj.value,
                snakeCaseObj.id
                )
        return new ProductDetail(-1, "", "", -1);
    }

}

export class Product {
    id?: number;
    name: string;
    price: number;
    imagePath?: string;
    productDetails?: ProductDetail[];
    static path = "product";

    constructor(name: string, price: number, imagePath: string, productDetails?: any, id?: number) {
        this.name = name;
        this.price = price;
        this.imagePath = imagePath;
        this.productDetails = productDetails;
        this.id = id;
    }

    public static mandatoryAttributes = ["name", "price"];

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
        let productDetailsList: ProductDetail[] = [];

        if (snakeCaseObj.product_details) {
            productDetailsList = snakeCaseObj.product_details.map((obj: Record<string, any>) => ProductDetail.fromSnakeCaseObject(obj))
        }

        console.log(productDetailsList)

        if (this.checkMandatoryAttributes(snakeCaseObj))
            return new Product(
                snakeCaseObj.name,
                snakeCaseObj.price,
                snakeCaseObj.image_path,
                productDetailsList,
                snakeCaseObj.id
                )
        return new Product("", 0, "", [], -1);
    }

    // static async loadById(id: number) {
    //     return await this.get(id).then((response) => {
    //         return response
    //     })
    // }


    static async getList(): Promise<Product[]> {
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

    static async get(id: number): Promise<Product> {
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
            path: Product.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        })
    }

    update() {
        return sendRequest({
            id: this.id,
            method: "PATCH",
            path: Product.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        })
    }

    delete() {
        return sendRequest({
            id: this.id,
            method: "DELETE",
            path: Product.path
        })
    }


}