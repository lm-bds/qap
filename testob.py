from dataclasses import dataclass, field

@dataclass
class TestGroup():
    cycle: str
    sitestests: field(default_factory=list)

    def add_sitetest(self, sitetests):
        self.sitestests.append(sitetests)

    def find_mean(self):
        return sitetests.result.mean()



class SiteTest(TestGroup):
    def __init__(self, cycle, result, site):
        super().__init__(cycle)
        self.result = result
        self.site = site