//const host = import.meta.env.VITE_API_HOST;


const headers = new Headers({
    "Content-Type": "application/json"
})

export function sendRequest(options: Record<string, any>) {
    let url = __API_URL__ + "/" + options.path;
    if (options.id !== undefined)
        url += "/" + options.id

    const request = new Request(url, {
        method: options.method,
        mode: "cors",
        credentials: "include",
        headers: headers,
        body: options.body
    })

    console.log(request)

    return fetch(url, {
        method: options.method,
        mode: "cors",
        credentials: "include",
        headers: headers,
        body: options.body
    })
}