const schoolListAPI = 'localhost:3000/school-list'

fetch(schoolListAPI)
  .then(response => {
    if (!response.ok) {
      throw new Error('oopsie whoopsie');
    }
  })
.then(data => {
  console.log(data);
})
.catch(error => {
  console.error('Error: ', error);
});