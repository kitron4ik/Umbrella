import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api/main/',
});

export default {
    login(data){
        return api.post('main/',data);
    },
};