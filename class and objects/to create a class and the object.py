class laptop:
    model_name=""
    os=""
    processor=""
laptop1=laptop()
laptop1.model_name='pavillion'
laptop1.processor='intel'
laptop1.os='windows11'

laptop2=laptop()
laptop2.model_name='mac air2'
laptop2.processor='Abionic13'
laptop2.os='mac os'
print(f"{laptop1.model_name} has {laptop1.processor} which runs on {laptop1.os}")
print(f"{laptop2.model_name} has {laptop2.processor} which runs on {laptop2.os}")
