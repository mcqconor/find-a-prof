function  getSchoolProfs(school) {
    return fetch(`http://192.168.1.8:3000/professors/school/${school}`)
        .then(response => response.json())
        .then(data => {
        return data; 
        })
        .catch(error => {
        throw error; 
        });
    }