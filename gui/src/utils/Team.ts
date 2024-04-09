import { Person } from './Person'

const host = import.meta.env.VITE_API_HOST;

const headers = new Headers({
    "Content-Type": "application/json"
})

export async function getTeamList() {
    return fetch(`${host}/teams`,{
        method: "GET",
        mode: "cors",
        credentials: "include"
    }).then((resp) => resp.json());
}

export async function createTeam(
    team: Team
) {
    return fetch(`${host}/team`,{
        method: "POST",
        mode: "cors",
        credentials: "include",
        headers: headers,
        body: JSON.stringify({
            leaderPersonId: team.leaderPerson.id })
    });
}


export class Team {
    id?: number;
    leaderPerson: Person;

    constructor(leaderPerson: Person) {
        this.leaderPerson = leaderPerson;
    }
}