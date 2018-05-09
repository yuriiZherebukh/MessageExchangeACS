import axios from "axios"

const loginUrl = '/api/v1/auth/login/';
const registerUrl = '/api/v1/auth/register/';
const logoutUrl = '/api/v1/auth/logout/';

export function loginService(email, password) {
    return axios.post(loginUrl, {
            email,
            password
        })
}

export function registerService(email, password, confirm_password, first_name, last_name) {
    return axios.post(registerUrl, {
            email,
            first_name,
            last_name,
            password,
            confirm_password,
        })
}
