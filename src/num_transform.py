import re
remap = dict(
    tb=re.compile('(?P<num>[0-9.]+)[ ]*TB'),
    gb=re.compile('(?P<num>[0-9.]+)[ ]*GB'),
    mb=re.compile('(?P<num>[0-9.]+)[ ]*MB'),
    kb=re.compile('(?P<num>[0-9.]+)[ ]*KB'),
    b=re.compile('(?P<num>[0-9.]+)[ ]*bytes')

)
convertmap = dict(
    tb=lambda x: float(x)*1024**4,
    gb=lambda x: float(x)*1024**3,
    mb=lambda x: float(x)*1024**2,
    kb=lambda x: float(x)*1024,
    b=lambda x: float(x)
)


def bytesstr2float(s: str):
    for k, v in remap.items():
        m = v.search(s)
        if m is not None:
            return convertmap[k](m.group('num'))
    return -2.0


percent_pattern = re.compile('(?P<num>[0-9.]+)[ ]*%')


def percentstr2float(s: str):
    m = percent_pattern.search(s)
    if m is not None:
        return float(m.group('num'))/100


def remove_comma(s: str):
    return float(s.replace(',', ''))


if __name__ == "__main__":
    print(bytesstr2float("12.2 GB"))
    print(bytesstr2float("12.2 bytes"))
    print(percentstr2float('22.2%'))
    print(percentstr2float('186.64 GB (37.93%)'))
    print(remove_comma('495,492'))
