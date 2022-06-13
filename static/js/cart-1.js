const updateBtn = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function (){
        const productId = this.dataset.product;
        const action = this.dataset.action;
        console.log('productId:', productId, 'action:', action)

        console.log('User: ' + user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending')
    //Url of the function update_item
    const url = '/update_item/'

    fetch(url,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data: ', data)
            location.reload()
        });

}