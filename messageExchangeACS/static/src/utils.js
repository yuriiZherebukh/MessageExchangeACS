import axios from "axios";


export let logged = () => sessionStorage.getItem('Authorization') != null;

export const EMAIL_REGEXP = /.+@.+\..+/;
export const ALPHA_REGEXP = /^[a-z]{0,20}$/i;
export const DIGIT_REGEXP = /^[0-9]{0,2}$/;


export const axiosInstance = axios.create({
        baseURL: 'http://192.168.64.128:8000/',
        headers: {
                    'Content-Type': 'application/json',
                    'Authorization': sessionStorage.getItem('Authorization')}
        });

export function emailIsNotValid(email) {
    if (email == '') {
            return 'This field is required';
        } else if (email.match(EMAIL_REGEXP) == null) {
            return 'Email fields is not in valid form';
        } else {
            return ''
        }
}

export function fieldIsEmpty(field) {
    return field == '' ? 'This field is required':'';
}

export function arrayIsEmpty(array) {
    return array.length == 0 ? 'This field is required':'';
}


const getCookie = (cookieName) => {
    var name = cookieName + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

export let userId = () => {
    let id = getCookie('user_id');
    id = id === "" ? null : +id;
    return id;
}

export function onlyAlpha(text) {
    if (ALPHA_REGEXP.test(text) == false) {
        return false;
    } else {
        return true
    }

}

export function onlyDigit(numbers) {
    if (DIGIT_REGEXP.test(numbers) == false) {
        return false;
    } else {
        return true
    }
}

