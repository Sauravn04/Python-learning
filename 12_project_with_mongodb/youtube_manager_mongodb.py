from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://nayaksaurav99:cFbMLBxd2oAwxKQW@cluster0.k9qivtr.mongodb.net/ytmanager",
)

print(client)
db = client["ytmanager"]

video_collections = db["ytvideos"]

# print(video_collections)


def list_videos():
    for video in video_collections.find():
        print(f"ID:{video['_id']},Name:{video['name']} and Time:{video['time']}")


def add_videos(name, time):
    video_collections.insert_one({"name": name, "time": time})
    print("Video added successfully")


def update_videos(video_id, new_name, new_time):
    video_collections.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}}
    )


def delete_videos(video_id):
    video_collections.delete_one({"_id": ObjectId(video_id)})
    print("Video deleted successfully!")


def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all Videos")
        print("2. Add a Videos")
        print("3. Update a Videos")
        print("4. Delete a Videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the time name: ")
            add_videos(name, time)
        elif choice == "3":
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated time name: ")
            update_videos(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video id to delete: ")
            delete_videos(video_id)

        elif choice == "5":
            print("Exit the app,Goodbye!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
