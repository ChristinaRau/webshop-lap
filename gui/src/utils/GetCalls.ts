const BASE_URL = "http://localhost:5000/";
const host = import.meta.env.VITE_API_HOST;

export function getBestTeam() {
    return fetch(
        BASE_URL + "max_team",
        {
            method: "GET"
        }
    )
}

export function getBestLeader() {
    return fetch(
        BASE_URL + "max_leader",
        {
            method: "GET"
        }
    )
}


export function getBestMember() {
    return fetch(
        BASE_URL + "max_member",
        {
            method: "GET"
        }
    )
}

export async function getPersonList() {
    return fetch(`${host}/persons`,{
        method: "GET",
        mode: "cors",
        credentials: "include"
    }).then((resp) => resp.json());
}
