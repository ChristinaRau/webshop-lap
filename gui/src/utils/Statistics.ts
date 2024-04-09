import { sendRequest } from "./Request.js";

export function getStatistics() {
    return sendRequest({
        method: "GET",
        path: "statistics"
    });
}