import fetch_comics
import post_wall


def main():
    file = fetch_comics.fetch_comics_img()
    message = fetch_comics.fetch_comics_comment()
    post_wall.post_photo(file, message)


if __name__ == "__main__":
    main()
