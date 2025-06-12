from pydantic import BaseModel


class CLIArgs(BaseModel):
    pass


def parse_args():
    return {}


def main():
    args = parse_args()
    print("Your args are:", args)


if __name__ == "__main__":
    main()