from helpers import  main_menu, add_post, add_comment, view_post_comments, search_posts



def cli():
  post_id = 1
  keyword = "post 1" 
  while True:
    main_menu()
    choice = input("Pick an option: ")

    if choice == "1":
      add_post()
      break
    elif choice == "2":
      add_comment(post_id)
      break
    elif choice == '3':
      view_post_comments(post_id)
      break
    elif choice == '4':
      search_posts(keyword)
      break
    elif choice == '5':
      print("Exiting....")
      break
    else:
        print("Invalid choice!")





if __name__ == "__main__":
  cli()
