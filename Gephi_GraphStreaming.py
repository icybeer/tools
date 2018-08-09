import urllib.request
import json


class GephiClient:
    ''' Examples from https://github.com/gephi/gephi/wiki/GraphStreaming
    # curl "http://localhost:8080/workspace0?operation=updateGraph" -d "{\"an\":{\"A\":{\"label\":\"Streaming Node A\"}}}"
    # {"an":{"A":{"label":"Streaming Node A","size":2}}} // add node A
    # {"an":{"B":{"label":"Streaming Node B","size":1}}} // add node B
    # {"ae":{"AB":{"source":"A","target":"B","directed":false,"weight":2}}} // add edge A->B
    # {"cn":{"A":{"size":2}}}  // changes the size attribute to 2
    # {"cn":{"B":{"label":null}}}  // removes the label attribute
    # {"ce":{"AB":{"label":"From A to B"}}} // add the label attribute
    # {"de":{"AB":{}}} // delete edge AB
    # {"dn":{"A":{}}}  // delete node A

    If a node is deleted, the edges connect to the node will be deleted automatically.
    '''

    def __init__(self, url):
        self.url = url + "?operation=updateGraph"
    
    def encode_json(self, attr_dict):
        return bytes(json.dumps(attr_dict), "utf-8")
    
    def update_graph(self, data):
        urllib.request.urlopen(self.url, data)

    def add_node(self, name, attr_dict):
        data = self.encode_json({"an": {name:attr_dict}})
        self.update_graph(data)
        return
    def add_edge(self, name, source, target, attr_dict):
        attr_dict.update({"source": source, "target": target})
        data = self.encode_json({"ae": {name:attr_dict}})
        self.update_graph(data)
        return
    def delete_edge(self, name):
        data = self.encode_json({"de": {name:{}}})
        self.update_graph(data)
        return
    def delete_node(self, name):
        data = self.encode_json({"dn": {name:{}}})
        self.update_graph(data)
        return
    def change_node(self, name, attr_dict):
        data = self.encode_json({"cn": {name:attr_dict}})
        self.update_graph(data)
        return
    def change_edge(self, name, attr_dict):
        data = self.encode_json({"ce": {name:attr_dict}})
        self.update_graph(data)
        return


if __name__ == "__main__":
    # Create GephiClient instance
    url = "http://localhost:8080/workspace2"
    client = GephiClient(url)
    
