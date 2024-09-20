def main():
    usr_input = input("File image: ").strip().lower()
    if usr_input.endswith("jpg") or usr_input.endswith("jpeg"):
        print("image/jepg")
    elif usr_input.endswith("gif"):
        print("image/gif")
    elif usr_input.endswith("png"):
        print("image/png")
    elif usr_input.endswith("pdf"):
        print("applicatipon/pdf")
    elif usr_input.endswith("txt"):
        print("text/plain")
    elif usr_input.endswith("zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()