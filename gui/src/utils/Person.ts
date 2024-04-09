const host = import.meta.env.VITE_API_HOST;

const headers = new Headers({
    "Content-Type": "application/json"
})

export async function getPersonList() {
    return fetch(`${host}/persons`,{
        method: "GET",
        mode: "cors",
        credentials: "include"
    }).then((resp) => resp.json());
}


export async function createPerson(
    person: Person
) {
    return fetch(`${host}/person`,{
        method: "POST",
        mode: "cors",
        credentials: "include",
        headers: headers,
        body: JSON.stringify({
            firstName: person.firstName,
            lastName: person.lastName })
    });
}


export class Person {
    id?: number;
    firstName: string;
    lastName: string;

    constructor(firstName: string, lastName: string) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}