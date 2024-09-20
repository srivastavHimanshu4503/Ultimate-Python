# Write a program to find out whether a given post is talking about “Harry” or not.
def check_about_Post(post):
    return True if "Harry".lower() in post.lower() else False

post1 = "I recently watched Harry Potter, and it was amazing!"
post2 = "The weather today is fantastic."

print(check_about_Post(post1))
print(check_about_Post(post2))