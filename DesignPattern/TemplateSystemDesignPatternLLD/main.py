
from abc import ABC, abstractmethod

class BuildPipeLine(ABC):

    def checkout(self):
        print(f"Checkout master branch")

    @abstractmethod
    def install_dependencies(self):
        pass

    @abstractmethod
    def compile(self):
        pass

    @abstractmethod
    def tests(self):
        pass

    @abstractmethod
    def deploy(self):
        pass

    def is_disployable(self):
        return False

    def run(self):
        self.checkout()
        self.install_dependencies()
        self.compile()
        self.tests()
        self.deploy()

class NodeJsPipeLine(BuildPipeLine):

    def install_dependencies(self):
        print(f"Nodejs dependencies installed")

    def compile(self):
        print(f"Nodejs compiling success")

    def tests(self):
        print(f"Nodejs tests success")

    def is_disployable(self):
        return True

    def deploy(self):
        if self.is_disployable():
            print(f"Nodejs diployable success")
        else:
            print(f"Nodejs diployable failed")

class JavaPipeLine(BuildPipeLine):

    def install_dependencies(self):
        print(f"Java dependencies installed")

    def compile(self):
        print(f"Java compiling success")

    def tests(self):
        print(f"Java tests success")

    def is_disployable(self):
        return False

    def deploy(self):
        if self.is_disployable():
            print(f"Java diployable success")
        else:
            print(f"Java diployable failed")



def main():
    nodejs_pipeline_class_obj = NodeJsPipeLine()
    nodejs_pipeline_class_obj.run()
    java_pipeline_class_obj = JavaPipeLine()
    java_pipeline_class_obj.run()

main()