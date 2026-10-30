from lab_classes import User, Tweet


def build_feed():
    # Accounts for a campus chess club
    maya = User('maya')
    rohan = User('rohan')
    users = [maya, rohan]

    # Posts, each authored by one of the users above
    posts = [
        Tweet('maya', 'Blitz tournament Friday at 7 #Chess #Blitz'),
        Tweet('rohan', 'Lost to the London System again #Chess #Rematch?'),
        Tweet('maya', 'Free coaching for anyone who beats me'),
    ]

    # Story: maya gains two followers, one leaves; rohan gains one.
    # The tournament post gets two likes; rohan's loss gets a pity like, then it's taken back.
    maya.follow()
    maya.follow()
    maya.unfollow()
    rohan.follow()

    posts[0].like()
    posts[0].like()
    posts[1].like()
    posts[1].unlike()

    return users, posts


def main():
    users, posts = build_feed()

    print('Accounts:')
    for user in users:
        print(user)

    print()
    print('Posts:')
    for post in posts:
        print(post)
        print('  hashtags:', post.hashtags())


if __name__ == '__main__':
    main()