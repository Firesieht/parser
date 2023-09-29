cards = document.getElementsByClassName('product-card__link j-card-link j-open-full-product-card')

arts = localStorage.getItem('arts')
if (arts == null){
    arts = []
} else{
    arts = JSON.parse(arts)
}

arts = []
for (card of cards){
    arts.push([card.href.split('/')[4]])
}
localStorage.setItem('arts', JSON.stringify(arts))

// cards = document.getElementsByClassName('product-card__link j-card-link j-open-full-product-card')
// for (card of cards){
//     arts.push(card.href.split('/')[4])
// }
