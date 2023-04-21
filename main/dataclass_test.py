from dataclasses import dataclass, fields

@dataclass(frozen=True, kw_only=True)
class Dataclass:
    a:int
    b:int
    c:int

data = Dataclass(a=1,b=3,c=5)
print(data) # 출력 : Dataclass(a=1, b=3, c=5)

print(data.a) # 1
print(data.b) # 3
print(data.c) # 5
print(fields(data))
