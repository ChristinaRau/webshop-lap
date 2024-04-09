
import { sendRequest } from "../Request";
import { camelToSnakeCase } from "../StringUtils";
import { Product } from "./Product";
import { Address, Customer } from "./Customer.js";

export class OrderProduct {
    id?: number;
    productId: number;
    orderId: number;
    product?: Product;
    order?: Order;

    static path = "order_product";

    constructor(productId: number, orderId: number, product?: Product, order?: Order, id?: number)
    {
        this.productId = productId;
        this.orderId = orderId;
        this.product = product;
        this.order = order;
        this.id = id;
    }

    public static mandatoryAttributes = ["order_id", "product_id"];

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
            return new OrderProduct(
                snakeCaseObj.product_id,
                snakeCaseObj.order_id
            );
        return new OrderProduct(-1, -1, -1);
    }

    create() {
        return sendRequest({
            method: "POST",
            path: OrderProduct.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        });
    }


}

export class Order {
    id?: number;
    deliveryAddress?: Address;
    paymentMethod?: string;
    customer?: Customer;
    dateOrdered?: string;
    orderProducts?: OrderProduct[];

    static path = "order";

    constructor(deliveryAddress: Address, paymentMethod: string, customer: Customer, dateOrdered: string, orderProducts: OrderProduct[], id?: number) {
        this.deliveryAddress = deliveryAddress;
        this.paymentMethod = paymentMethod;
        this.customer = customer;
        this.dateOrdered = dateOrdered;
        this.orderProducts = orderProducts;
        this.id = id;
    }

    public static mandatoryAttributes = ["delivery_address_id", "payment_method", "customer_id"];

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
        let orderProductsList: OrderProduct[] = [];

        if (snakeCaseObj.order_products) {
            orderProductsList = snakeCaseObj.order_products.map((obj: Record<string, any>) => OrderProduct.fromSnakeCaseObject(obj));
        }

        if (snakeCaseObj.delivery_address) {
            snakeCaseObj.delivery_address = Address.fromSnakeCaseObject(snakeCaseObj.delivery_address);
        }

        if (snakeCaseObj.customer) {
            snakeCaseObj.customer = Customer.fromSnakeCaseObject(snakeCaseObj.customer);
        }


        console.log(orderProductsList);

        if (this.checkMandatoryAttributes(snakeCaseObj))
            return new Order(
                snakeCaseObj.delivery_address,
                snakeCaseObj.payment_method,
                snakeCaseObj.customer,
                snakeCaseObj.date_ordered,
                orderProductsList,
                snakeCaseObj.id
            );
        return new Order(new Address("", "", "", "", "", "", "", -1), "", new Customer("", "", undefined, -1), "", [], -1);
    }

    static async getList(): Promise<Order[]> {
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

    static async get(id: number): Promise<Order> {
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
            path: Order.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        });
    }

    update() {
        return sendRequest({
            id: this.id,
            method: "PATCH",
            path: Order.path,
            body: JSON.stringify(this.toSnakeCaseObject())
        });
    }

    delete() {
        return sendRequest({
            id: this.id,
            method: "DELETE",
            path: Order.path
        });
    }


}