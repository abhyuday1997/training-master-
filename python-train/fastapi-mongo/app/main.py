import uvicorn
# importing sys
import sys
  
# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'E:\coursera\Data analytics\python_training\git_practice\training-master-\python-train\fasapi-mongo\app\server')

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
