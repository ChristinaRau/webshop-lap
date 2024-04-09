const host = import.meta.env.VITE_API_HOST;


export async function login(username: string, password: string) {
    let formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    
    return fetch(`${host}/login`, {
        method: "POST",
        mode: "cors",
        credentials: "include",
        body: formData
    }).then((response) => {
        return response.ok;
    });
}

export async function checkLogin() {
    return fetch(`${host}/check_login`, {
        method: "GET",
        mode: "cors",
        credentials: "include"
    }).then((resp) => resp.json())
    .then(resp => resp.is_authenticated);
}