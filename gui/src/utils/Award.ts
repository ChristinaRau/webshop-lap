const host = import.meta.env.VITE_API_HOST;

const headers = new Headers({
    "Content-Type": "application/json"
})

export async function getAwardList() {
    return fetch(`${host}/awards`,{
        method: "GET",
        mode: "cors",
        credentials: "include"
    }).then((resp) => resp.json());
}

export async function createAward(
    award: Award
) {
    return fetch(`${host}/award`,{
        method: "POST",
        mode: "cors",
        credentials: "include",
        headers: headers,
        body: JSON.stringify({
            pointsPerMember: award.pointsPerMember,
            pointsPerLeader: award.pointsPerLeader })
    });
}


export class Award {
    id?: number;
    pointsPerMember: string;
    pointsPerLeader: string;

    constructor(pointsPerMember: string, pointsPerLeader: string) {
        this.pointsPerMember = pointsPerMember;
        this.pointsPerLeader = pointsPerLeader;
    }
}