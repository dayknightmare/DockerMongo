import axios from "axios"

export default function ({ }, inject) {
    const api = axios.create({
        baseURL: process.env.API_URL,
    })

    inject("api", {
        api: api,
    })
}
