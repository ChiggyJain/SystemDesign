
from abc import ABC, abstractmethod

class FileSystemNode(ABC):

    name: str = ""
    type_of_file_system_node: str = "File"

    def __init__(self, name: str, type_of_file_system_node: str):
        self.name = name
        self.type_of_file_system_node = type_of_file_system_node

    def get_name(self):
        return self.name

    def get_file_system_node_type(self):
        return self.type_of_file_system_node
    
    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_content(self):
        pass

    


class File(FileSystemNode):

    def __init__(self, name: str, bytes: str, content: str):
        super().__init__(name, "File")
        self.content = content
        self.bytes = bytes

    def get_size(self):
        return self.bytes

    def get_content(self):
        return self.content


class Directory(FileSystemNode):

    def __init__(self, name: str):
        super().__init__(name, "Directory")
        self.total_size = 0
        self.childrens_file_system_node_class_obj = []

    def add(self, file_system_node_class_obj: FileSystemNode):
        self.childrens_file_system_node_class_obj.append(file_system_node_class_obj)
        self.total_size = self.get_size()

    def get_size(self):
        self.total_size = 0
        for each_file_system_node_class_obj in self.childrens_file_system_node_class_obj:
            self.total_size+= each_file_system_node_class_obj.get_size()
        return self.total_size

    def get_content(self):
        contents = []
        for each_file_system_node_class_obj in self.childrens_file_system_node_class_obj:
            contents.append(
                f"{each_file_system_node_class_obj.get_file_system_node_type()}: {each_file_system_node_class_obj.get_name()}, Size: {each_file_system_node_class_obj.get_size()}, Content: {each_file_system_node_class_obj.get_content()}"
            )
        return contents




def main():

    services_directory_class_obj = Directory("services")
    services_directory_class_obj.add(File("auth_services.py", 100, "Auth services file content"))
    services_directory_class_obj.add(File("user_services.py", 100, "User services file content"))
    
    repository_directory_class_obj = Directory("repository")
    repository_directory_class_obj.add(File("auth_repository.py", 100, "Auth repository file content"))
    repository_directory_class_obj.add(File("user_repository.py", 100, "User repository file content"))

    root_directory_class_obj = Directory("IRTCProject")
    root_directory_class_obj.add(File("README.MD", 100, "Readme file content"))
    root_directory_class_obj.add(services_directory_class_obj)
    root_directory_class_obj.add(repository_directory_class_obj)

    print(f"Directory: {root_directory_class_obj.get_name()}, Size: {root_directory_class_obj.get_size()}, Content: {root_directory_class_obj.get_content()}")



main()