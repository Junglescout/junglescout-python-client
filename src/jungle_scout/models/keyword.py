from jungle_scout.base_model import BaseModel


class Keyword(BaseModel):
    def _update_attributes(self, data):
        self.git_url = data["git_url"]
        self.html_url = data["html_url"]
        self.name = data["name"]
        self.path = data["path"]
        self.score = data["score"]
        self.sha = data["sha"]
        self.text_matches = data.get("text_matches", [])
