// probably move this to a separate file
Array.prototype.move = function(from, to) {
    this.splice(to, 0, this.splice(from, 1)[0]);
};

function Article() {
  this.id = -1; // article is not assigned a unique id until added to a newsletter object
  this.title = "";
  this.articleLink = "";
  this.byline = "";
  this.contentPreview = "";
  this.thumbnailLink = "";
  this.thumbnailCaption = "";
  this.thumbnailCredit = "";
}

function Newsletter() {
  this.date = new Date();
  this.intro = "";
  this.emailPreview = "";
  this.errata = "";
  this.articleOrder = [];
  this.highestID = -1;
  this.articles = [];

  this.add = function(article) {
    this.highestID++;
    article.id = this.highestID;
    this.articles.push(article);
    this.articleOrder.push(article.id);
  }

  this.move = function(id, newPosition) {
    oldPosition = this.articleOrder.indexOf(id);
    if (oldPosition != -1) {
      this.articleOrder.move(oldPosition, newPosition)
    } else {
      throw "Article ID not found in articleOrder"
    }
  }

  this.delete = function(id) {
    orderPosition = this.articleOrder.indexOf(id);
    articlesPosition = this.articles.findIndex(element => element.id == id);
    if (orderPosition != -1 && articlesPosition != -1) {
      this.articleOrder.splice(orderPosition, 1);
      this.articles.splice(articlesPosition, 1);
    } else {
      throw "Article ID not found in either articleOrder or articles"
    }
  }
}

function fromJSON() {

}

function toMJML() {

}

var news = new Newsletter();
var art1 = new Article();
var art2 = new Article();
var art3 = new Article();

news.add(art1);
news.add(art2);
news.add(art3);
