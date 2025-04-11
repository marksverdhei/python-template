from pydantic import BaseModel

class CLIArgs(BaseModel):
    pass
def parse_args():
    return {}


if __name__ == "__main__":
    args = parse_args()
    print("Your args are:", args)