import { sendRequest } from "./Request.js";

export function getBillingInformation(orderId: number) {
    return sendRequest({
        method: "GET",
        path: "billing/order",
        id: orderId
    });
}