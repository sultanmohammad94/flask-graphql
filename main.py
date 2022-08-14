from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="Stranger"))
    goodbye = String()
    
    def reslove_hello(root, info, name):
        return f"Hello {name}"
    
    def resolve_goodbye(root, info):
        return "Good Bye"


def main():    
    schema = Schema(query=Query)
    query_str = "{hello}"
    result = schema.execute(query_str)
    print('result = ', result)
    query_with_args = '{hello(name:"mhd khair sultan")}'
    result2 = schema.execute(query_with_args)
    print('result2 = ', result2)
    

if __name__ == "__main__":
    main()
