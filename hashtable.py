class HashTable:

    def __init__(self, buckets):
        self.buckets = buckets
        self.table = [[] for i in range(self.buckets)]

    def buckets_str(self):
        """
        Return a string representing the various buckets of this table. The output looks like:
          0000->
          0001->
          0002->
          0003->parrt:99
          0004->
        where parrt:99 indicates an association of (parrt,99) in bucket 3.
        """
        buckets_index = ""
        counter = 0
        for bucket in self.table:
            buckets_index += "%04d->" % counter

            pairs = []
            for pair in bucket:
                pairs.append(":".join([str(pair[0]), str(pair[1])]))
            buckets_index += ", ".join(pairs) + '\n'
            counter += 1
        return buckets_index

    def __str__(self):
        """
        Return what str(table) would return for a regular Python dict such as {parrt:99}.
        The order should be bucket order and then insertion order in the bucket.
        The insertion order is guaranteed when you append to the buckets in put.
        """
        b = []
        if len(self.table) == 0:
            return "{}"

        for buck in self.table:
            for pair in buck:
                a = str(pair[0]) + ":" + str(pair[1])
                b.append(a)
        result = ', '.join(b)
        result = "{" + result + "}"
        if result == "":
            return "{" + result + "}"
        return result

    def get(self, key):
        """
        Return table[key].
        Find the appropriate bucket indicated by the key and look for the association with the key.
        Return the value (not the key and not the association!)
        Return None if key not found.
        """
        a, b, c = self.bucket_indexof(self.table, key)
        if b == False:
            return (set())
        else:
            return (self.table[c][a][1])

    def put(self, key, value):
        """
        Perform table[key] = value
        Find the appropriate bucket indicated by key and then append a value to the bucket.
        If the bucket for key already has a key, value pair with that key then replace it.
        Make sure that you are only adding (key, value) associations to the buckets.
        """
        a, b, c = self.bucket_indexof(key)
        if b == True:
            a, b, c = self.bucket_indexof(key)
            self.table[c][a][1].update(value)
            return None

        elif b == False:
            self.table[c].append((key, value))
            return None

    def bucket_indexof(self, key):
        """
        Return the element within a specific bucket; the bucket is table[key].
        You have to search the bucket linearly.
        """
        tuple_index = 0
        if type(key) == int:
            hashcode = key

        elif type(key) == str:
            hashcode = 0
            for i in key:
                hashcode = hashcode * 31 + ord(i)

        else:
            hashcode = None

        buck_number = hashcode % len(self.table)
        buck = self.table[buck_number]

        exists = False
        for elem in buck:
            if key == elem[0]:
                tuple_index = buck.index(elem)
                exists = True
        return tuple_index, exists, buck_number
