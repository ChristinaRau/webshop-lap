import { camelToSnakeCase } from "./StringUtils";

const host = import.meta.env.VITE_API_HOST;

const headers = new Headers({
    "Content-Type": "application/json"
})

// export async function getComputerBaseModelList() {
//     return fetch(`${host}/computerbasemodels`,{
//         method: "GET",
//         mode: "cors",
//         credentials: "include"
//     }).then((resp) => resp.json());
// }


// export async function createComputerBaseModel(
//     computerbasemodel: ComputerBaseModel
// ) {
//     return fetch(`${host}/computerbasemodel`,{
//         method: "POST",
//         mode: "cors",
//         credentials: "include",
//         headers: headers,
//         body: JSON.stringify({
//             firstName: computerbasemodel.firstName,
//             lastName: computerbasemodel.lastName })
//     });
// }

function sendRequest(options: Record<string, any>) {
    let url = `${host}/computer-base-model`;
    if (options.id !== undefined)
        url += "/" + options.id

    const request = new Request(url, {
        method: options.method,
        mode: "cors",
        credentials: "include",
        headers: headers,
        body: options.body
    })

    return fetch(request)
}

export class ComputerBaseModel {
    id?: number;
    name: string;
    processor: string;

    constructor(name: string, processor: string, id: number) {
        this.name = name;
        this.processor = processor;
        this.id = id;
    }

    public toSnakeCaseObject() {
        const newObject = <Record<string, any>>{}
        for (const key in this) {
            newObject[camelToSnakeCase(key)] = this[key]
        }

        return newObject;
    }

    static async loadById(id: number) {
        return await this.get(id).then((response) => {
            return response.json()
        }).then((result) => {
            return new ComputerBaseModel(
                result.name,
                result.processor,
                id
            )
        })
    }

    static get(id: number) {
        return sendRequest({
            id:  id,
            method: "GET"
        })
    }

    create() {
        return sendRequest({
            method: "POST",
            body: JSON.stringify(this.toSnakeCaseObject())
        })
    }

    update() {
        return sendRequest({
            id: this.id,
            method: "PATCH",
            body: JSON.stringify(this.toSnakeCaseObject())
        })
    }

    delete() {
        return sendRequest({
            id: this.id,
            method: "DELETE",
            body: JSON.stringify(this.toSnakeCaseObject())
        })
    }


}