export function  makeSchoolAPICall() {
    return fetch('http://192.168.1.8:3000/school-list')
        .then(response => response.json())
        .then(data => {
        return data; 
        })
        .catch(error => {
        throw error; 
        });
    }