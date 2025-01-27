class SimpleHashSet():
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]  # buckets

    def hash_function(self, value):
        return sum([ord(char) for char in value]) % self.size  # hash code -> index
    
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    
    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def print_set(self):
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index} : {bucket}")

hashset = SimpleHashSet(10)
hashset.add("Martin")
hashset.add("Lukas")
hashset.add("Rodriguez")
hashset.print_set()
print(hashset.contains("Lukas"))
print(hashset.contains("lukas"))
hashset.remove("Martin")
hashset.contains("Martin")
print(hashset.buckets[2])
