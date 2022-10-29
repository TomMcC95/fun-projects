import instaloader

ig = instaloader.Instaloader()

dp = "jessica_readdiefitness"

profile = instaloader.Profile.from_username(ig.context, dp)
print('start')
for post in profile.get_posts():
    ig.download_post(post, target=profile.username)
print('finish')