
import { sendRequest } from "../Request";
import { camelToSnakeCase } from "../StringUtils";

export class Address {
    id?: number;
    firstName: string;
    lastName: string;
    street: string;
    houseNumber: string;
    city: string;
    postalCode: string;
    country?: string;

    constructor(firstName: string, lastName: string, street: string, houseNumber: string, city: string, postalCode: string, country?: string, id?: number) {    
        this.firstName = firstName;
        this.lastName = lastName;
        this.street = street;
        this.houseNumber = houseNumber;
        this.city = city;
        this.postalCode = postalCode;
        this.country = country;
        this.id = id;
    }

    public static mandatoryAttributes = ["first_name", "last_name", "street", "house_number", "city", "postal_code"];

    public static checkMandatoryAttributes(obj: Record<string, any>) {
        return this.mandatoryAttributes.every((el) => Object.keys(obj).includes(el));
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
            return new Address(
                snakeCaseObj.first_name,
                snakeCaseObj.last_name,
                snakeCaseObj.street,
                snakeCaseObj.house_number,
                snakeCaseObj.city,
                snakeCaseObj.postal_code,
                snakeCaseObj.country,
                snakeCaseObj.id
            );
        return new Address("", "", "", "", "", "", "", -1);
    }

}

export class Customer {
    id?: number;
    emailAddress: string;
    telNumber?: string;
    billingAddress?: Address;

    constructor(emailAddress: string, telNumber?: string, billingAddress?: Address, id?: number) {
        this.emailAddress = emailAddress;
        this.telNumber = telNumber;
        this.billingAddress = billingAddress;
        this.id = id;
    }

    public static mandatoryAttributes = ["email_address"];

    public static checkMandatoryAttributes(obj: Record<string, any>) {
        return this.mandatoryAttributes.every((el) => Object.keys(obj).includes(el));
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
        let billingAddress: Address | undefined;

        if (snakeCaseObj.billing_address) {
            billingAddress = Address.fromSnakeCaseObject(snakeCaseObj.billing_address);
        }

        console.log(billingAddress);

        if (this.checkMandatoryAttributes(snakeCaseObj))
            return new Customer(
                snakeCaseObj.email_address,
                snakeCaseObj.tel_number,
                snakeCaseObj.billing_address,
                snakeCaseObj.id
            );
        return new Customer("", "", undefined, -1);
    }

    // static async loadById(id: number) {
    //     return await this.get(id).then((response) => {
    //         return response
    //     })
    // }


    static async getList(): Promise<Customer[]> {
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

    static async get(id: number): Promise<Customer> {
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
            path: Customer.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        });
    }

    update() {
        return sendRequest({
            id: this.id,
            method: "PATCH",
            path: Customer.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        });
    }

    delete() {
        return sendRequest({
            id: this.id,
            method: "DELETE",
            path: Customer.path
        });
    }


}