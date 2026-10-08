from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
app = FastAPI()

text_posts = {
     1 : {"title" : "New Post", "content" : "cool test post"},
     2 : {"title" : "Python Tip", "content" : "Use list comprehensions for cleaner code"},    
     3 : {"title" : "Daily Motivation", "content" : "Consistency is key to success"},
     4 : {"title" : "Fun Fact", "content" : "The first computer virus was created in 1986 and was called the Brain virus."},
     5 : {"title" : "Tech News", "content" : "The latest iPhone model has been released with improved camera features."},
     6 : {"title" : "Travel Guide", "content" : "Top 10 destinations to visit in Europe this summer."},
     7 : {"title" : "Healthy Living", "content" : "Incorporate more fruits and vegetables into your diet for better health."},
     8 : {"title" : "Book Recommendation", "content" : "The Alchemist by Paulo Coelho is a must-read for anyone seeking inspiration."},
     9 : {"title" : "Movie Review", "content" : "The latest Marvel movie is a visual spectacle with a compelling storyline."},
    10 : {"title" : "Fitness Tip", "content" : "Incorporate strength training into your workout routine for better overall fitness."}
     }


@app.get("/posts")
def get_all_posts(limit: int, content_length: str):
    if limit:
        return list(text_posts.values())[:limit]
    
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code= 404, detail = "Post Not Found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    pass 


