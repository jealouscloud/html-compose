"""

These are assumptions that are used elsewhere in the repo
They usually have no bearing on the code functionality itself

"""

from time import perf_counter

import pytest


def test_args():
    """
    This is the logic that base_element.append uses for args
    """
    input_data = (1, 2, 3, 4, 5)

    def demo(*args):
        # If you pass a tuple manually, it needs to be unboxed
        if (
            isinstance(args, tuple)
            and len(args) == 1
            and isinstance(args[0], tuple)
        ):
            return args[0]
        return args

    # demo(1,2,3)
    assert demo(*input_data) == input_data
    assert demo(1, 2, 3, 4, 5) == input_data
    assert demo(input_data) == input_data


def test_join_perf():
    """
    We use an LRU cache to speed up the join_attr function

    This test confirms the hypothesis that the cache is faster than no cache
    As long as there are attrs that are frequently used

    This is implemented in ElementBase

    """
    import random
    import string
    from functools import lru_cache

    random.seed(0)
    ATTRS_PER_ELEMENT = 10000
    TOP_ATTR_COUNT = 100
    ATTR_MAX_SIZE = 100
    ELEMENT_COUNT = 10

    def generate_random_string(length: int) -> str:
        return "".join(
            random.choices(string.ascii_letters + string.digits, k=length)
        )

    def generate_attrs(count, max_size):
        keys = [generate_random_string(10) for _ in range(count)]
        values = [
            generate_random_string(random.randint(1, max_size))
            for _ in range(count)
        ]
        attr_dict = {}
        for i in range(count):
            attr_dict[keys[i]] = values[i]
        return attr_dict

    # Generate a bunch of pseudo elements
    pseudo_elements = [
        generate_attrs(ATTRS_PER_ELEMENT, ATTR_MAX_SIZE)
        for _ in range(ELEMENT_COUNT)
    ]

    def join_attr(key, value):
        return f'{key}="{value}"'

    start = perf_counter()
    for element in pseudo_elements:
        _ = " ".join((join_attr(k, v) for k, v in element.items()))

    end = perf_counter()
    no_cache = end - start
    print(f"\nTime taken without cache: {end - start}")
    top_attrs = generate_attrs(TOP_ATTR_COUNT, ATTR_MAX_SIZE)
    infrequent_attrs = generate_attrs(10000, 100)  # Big spread
    infr_keys = list(infrequent_attrs.keys())

    pseudo_elements = []
    attr_delta = ATTRS_PER_ELEMENT - TOP_ATTR_COUNT

    for _ in range(ELEMENT_COUNT):
        el = top_attrs.copy()
        infreq_selected = []
        for k in [
            random.choice(infr_keys)
            for _ in range(ATTRS_PER_ELEMENT - TOP_ATTR_COUNT)
        ]:
            infreq_selected.append((k, infrequent_attrs[k]))

        ratio = attr_delta / TOP_ATTR_COUNT
        infreq_i = 0
        for k, v in top_attrs.items():
            el[k] = v
            # Add infrequent attrs
            for _ in range(int(ratio)):
                ifq = infreq_selected[infreq_i]
                el[ifq[0]] = ifq[1]
        pseudo_elements.append(el)

    join_attr = lru_cache(maxsize=TOP_ATTR_COUNT)(join_attr)

    start = perf_counter()
    for element in pseudo_elements:
        _ = " ".join((join_attr(k, v) for k, v in element.items()))

    end = perf_counter()
    print(f"Time taken with cache: {end - start}")

    with_cache = end - start

    assert with_cache < no_cache, "Cache should be faster than no cache"


def test_yield_from():
    arr = [1, 2, 3, 4, 5]

    def gen():
        yield from arr

    assert list(gen()) == arr

    gen_2 = (x for x in arr)
    assert list(gen_2) == arr


@pytest.mark.skip(reason="Performance test")
def test_compare_argument_style_performance():
    """
    This test compares a big arg list vs kwargs
    We do a lot of if not (x is None or x is False) checks
    The test confirms that a big arg list is comparable to unpacking a kwargs
    dict

    It would be way better to use a kwargs dict, but our branch to use
    Unpack[TypedDict] for named kwargs is not supported in python <3.12

    I tried using typing_extensions but the language server Pylance wasn't happy

    So we have to use a big arg list for now
    """

    def process_attr(name, value):
        pass

    # emulate our class_ problem
    special_list = {"ik_": "ik", "in_": "in", "is_": "is", "as_": "as"}

    def fn2(**kwargs):
        nonlocal special_list
        for k, v in kwargs.items():
            process_attr(special_list.get(k, k), v)

    def fn1(
        aa=None,
        ab=None,
        ac=None,
        ad=None,
        ae=None,
        af=None,
        ag=None,
        ah=None,
        ai=None,
        aj=None,
        ak=None,
        al=None,
        am=None,
        an=None,
        ao=None,
        ap=None,
        aq=None,
        ar=None,
        at=None,
        au=None,
        av=None,
        aw=None,
        ax=None,
        ay=None,
        az=None,
        ba=None,
        bb=None,
        bc=None,
        bd=None,
        be=None,
        bf=None,
        bg=None,
        bh=None,
        bi=None,
        bj=None,
        bk=None,
        bl=None,
        bm=None,
        bn=None,
        bo=None,
        bp=None,
        bq=None,
        br=None,
        bs=None,
        bt=None,
        bu=None,
        bv=None,
        bw=None,
        bx=None,
        by=None,
        bz=None,
        ca=None,
        cb=None,
        cc=None,
        cd=None,
        ce=None,
        cf=None,
        cg=None,
        ch=None,
        ci=None,
        cj=None,
        ck=None,
        cl=None,
        cm=None,
        cn=None,
        co=None,
        cp=None,
        cq=None,
        cr=None,
        cs=None,
        ct=None,
        cu=None,
        cv=None,
        cw=None,
        cx=None,
        cy=None,
        cz=None,
        da=None,
        db=None,
        dc=None,
        dd=None,
        de=None,
        df=None,
        dg=None,
        dh=None,
        di=None,
        dj=None,
        dk=None,
        dl=None,
        dm=None,
        dn=None,
        do=None,
        dp=None,
        dq=None,
        dr=None,
        ds=None,
        dt=None,
        du=None,
        dv=None,
        dw=None,
        dx=None,
        dy=None,
        dz=None,
        ea=None,
        eb=None,
        ec=None,
        ed=None,
        ee=None,
        ef=None,
        eg=None,
        eh=None,
        ei=None,
        ej=None,
        ek=None,
        el=None,
        em=None,
        en=None,
        eo=None,
        ep=None,
        eq=None,
        er=None,
        es=None,
        et=None,
        eu=None,
        ev=None,
        ew=None,
        ex=None,
        ey=None,
        ez=None,
        fa=None,
        fb=None,
        fc=None,
        fd=None,
        fe=None,
        ff=None,
        fg=None,
        fh=None,
        fi=None,
        fj=None,
        fk=None,
        fl=None,
        fm=None,
        fn=None,
        fo=None,
        fp=None,
        fq=None,
        fr=None,
        fs=None,
        ft=None,
        fu=None,
        fv=None,
        fw=None,
        fx=None,
        fy=None,
        fz=None,
        ga=None,
        gb=None,
        gc=None,
        gd=None,
        ge=None,
        gf=None,
        gg=None,
        gh=None,
        gi=None,
        gj=None,
        gk=None,
        gl=None,
        gm=None,
        gn=None,
        go=None,
        gp=None,
        gq=None,
        gr=None,
        gs=None,
        gt=None,
        gu=None,
        gv=None,
        gw=None,
        gx=None,
        gy=None,
        gz=None,
        ha=None,
        hb=None,
        hc=None,
        hd=None,
        he=None,
        hf=None,
        hg=None,
        hh=None,
        hi=None,
        hj=None,
        hk=None,
        hl=None,
        hm=None,
        hn=None,
        ho=None,
        hp=None,
        hq=None,
        hr=None,
        hs=None,
        ht=None,
        hu=None,
        hv=None,
        hw=None,
        hx=None,
        hy=None,
        hz=None,
        ia=None,
        ib=None,
        ic=None,
        id=None,
        ie=None,
        if_=None,
        ig=None,
        ih=None,
        ii=None,
        ij=None,
        ik=None,
        il=None,
        im=None,
        in_=None,
        io=None,
    ):
        if not (aa is None or aa is False):
            process_attr("aa", aa)
        if not (ab is None or ab is False):
            process_attr("ab", ab)
        if not (ac is None or ac is False):
            process_attr("ac", ac)
        if not (ad is None or ad is False):
            process_attr("ad", ad)
        if not (ae is None or ae is False):
            process_attr("ae", ae)
        if not (af is None or af is False):
            process_attr("af", af)
        if not (ag is None or ag is False):
            process_attr("ag", ag)
        if not (ah is None or ah is False):
            process_attr("ah", ah)
        if not (ai is None or ai is False):
            process_attr("ai", ai)
        if not (aj is None or aj is False):
            process_attr("aj", aj)
        if not (ak is None or ak is False):
            process_attr("ak", ak)
        if not (al is None or al is False):
            process_attr("al", al)
        if not (am is None or am is False):
            process_attr("am", am)
        if not (an is None or an is False):
            process_attr("an", an)
        if not (ao is None or ao is False):
            process_attr("ao", ao)
        if not (ap is None or ap is False):
            process_attr("ap", ap)
        if not (aq is None or aq is False):
            process_attr("aq", aq)
        if not (ar is None or ar is False):
            process_attr("ar", ar)
        if not (at is None or at is False):
            process_attr("at", at)
        if not (au is None or au is False):
            process_attr("au", au)
        if not (av is None or av is False):
            process_attr("av", av)
        if not (aw is None or aw is False):
            process_attr("aw", aw)
        if not (ax is None or ax is False):
            process_attr("ax", ax)
        if not (ay is None or ay is False):
            process_attr("ay", ay)
        if not (az is None or az is False):
            process_attr("az", az)
        if not (ba is None or ba is False):
            process_attr("ba", ba)
        if not (bb is None or bb is False):
            process_attr("bb", bb)
        if not (bc is None or bc is False):
            process_attr("bc", bc)
        if not (bd is None or bd is False):
            process_attr("bd", bd)
        if not (be is None or be is False):
            process_attr("be", be)
        if not (bf is None or bf is False):
            process_attr("bf", bf)
        if not (bg is None or bg is False):
            process_attr("bg", bg)
        if not (bh is None or bh is False):
            process_attr("bh", bh)
        if not (bi is None or bi is False):
            process_attr("bi", bi)
        if not (bj is None or bj is False):
            process_attr("bj", bj)
        if not (bk is None or bk is False):
            process_attr("bk", bk)
        if not (bl is None or bl is False):
            process_attr("bl", bl)
        if not (bm is None or bm is False):
            process_attr("bm", bm)
        if not (bn is None or bn is False):
            process_attr("bn", bn)
        if not (bo is None or bo is False):
            process_attr("bo", bo)
        if not (bp is None or bp is False):
            process_attr("bp", bp)
        if not (bq is None or bq is False):
            process_attr("bq", bq)
        if not (br is None or br is False):
            process_attr("br", br)
        if not (bs is None or bs is False):
            process_attr("bs", bs)
        if not (bt is None or bt is False):
            process_attr("bt", bt)
        if not (bu is None or bu is False):
            process_attr("bu", bu)
        if not (bv is None or bv is False):
            process_attr("bv", bv)
        if not (bw is None or bw is False):
            process_attr("bw", bw)
        if not (bx is None or bx is False):
            process_attr("bx", bx)
        if not (by is None or by is False):
            process_attr("by", by)
        if not (bz is None or bz is False):
            process_attr("bz", bz)
        if not (ca is None or ca is False):
            process_attr("ca", ca)
        if not (cb is None or cb is False):
            process_attr("cb", cb)
        if not (cc is None or cc is False):
            process_attr("cc", cc)
        if not (cd is None or cd is False):
            process_attr("cd", cd)
        if not (ce is None or ce is False):
            process_attr("ce", ce)
        if not (cf is None or cf is False):
            process_attr("cf", cf)
        if not (cg is None or cg is False):
            process_attr("cg", cg)
        if not (ch is None or ch is False):
            process_attr("ch", ch)
        if not (ci is None or ci is False):
            process_attr("ci", ci)
        if not (cj is None or cj is False):
            process_attr("cj", cj)
        if not (ck is None or ck is False):
            process_attr("ck", ck)
        if not (cl is None or cl is False):
            process_attr("cl", cl)
        if not (cm is None or cm is False):
            process_attr("cm", cm)
        if not (cn is None or cn is False):
            process_attr("cn", cn)
        if not (co is None or co is False):
            process_attr("co", co)
        if not (cp is None or cp is False):
            process_attr("cp", cp)
        if not (cq is None or cq is False):
            process_attr("cq", cq)
        if not (cr is None or cr is False):
            process_attr("cr", cr)
        if not (cs is None or cs is False):
            process_attr("cs", cs)
        if not (ct is None or ct is False):
            process_attr("ct", ct)
        if not (cu is None or cu is False):
            process_attr("cu", cu)
        if not (cv is None or cv is False):
            process_attr("cv", cv)
        if not (cw is None or cw is False):
            process_attr("cw", cw)
        if not (cx is None or cx is False):
            process_attr("cx", cx)
        if not (cy is None or cy is False):
            process_attr("cy", cy)
        if not (cz is None or cz is False):
            process_attr("cz", cz)
        if not (da is None or da is False):
            process_attr("da", da)
        if not (db is None or db is False):
            process_attr("db", db)
        if not (dc is None or dc is False):
            process_attr("dc", dc)
        if not (dd is None or dd is False):
            process_attr("dd", dd)
        if not (de is None or de is False):
            process_attr("de", de)
        if not (df is None or df is False):
            process_attr("df", df)
        if not (dg is None or dg is False):
            process_attr("dg", dg)
        if not (dh is None or dh is False):
            process_attr("dh", dh)
        if not (di is None or di is False):
            process_attr("di", di)
        if not (dj is None or dj is False):
            process_attr("dj", dj)
        if not (dk is None or dk is False):
            process_attr("dk", dk)
        if not (dl is None or dl is False):
            process_attr("dl", dl)
        if not (dm is None or dm is False):
            process_attr("dm", dm)
        if not (dn is None or dn is False):
            process_attr("dn", dn)
        if not (do is None or do is False):
            process_attr("do", do)
        if not (dp is None or dp is False):
            process_attr("dp", dp)
        if not (dq is None or dq is False):
            process_attr("dq", dq)
        if not (dr is None or dr is False):
            process_attr("dr", dr)
        if not (ds is None or ds is False):
            process_attr("ds", ds)
        if not (dt is None or dt is False):
            process_attr("dt", dt)
        if not (du is None or du is False):
            process_attr("du", du)
        if not (dv is None or dv is False):
            process_attr("dv", dv)
        if not (dw is None or dw is False):
            process_attr("dw", dw)
        if not (dx is None or dx is False):
            process_attr("dx", dx)
        if not (dy is None or dy is False):
            process_attr("dy", dy)
        if not (dz is None or dz is False):
            process_attr("dz", dz)
        if not (ea is None or ea is False):
            process_attr("ea", ea)
        if not (eb is None or eb is False):
            process_attr("eb", eb)
        if not (ec is None or ec is False):
            process_attr("ec", ec)
        if not (ed is None or ed is False):
            process_attr("ed", ed)
        if not (ee is None or ee is False):
            process_attr("ee", ee)
        if not (ef is None or ef is False):
            process_attr("ef", ef)
        if not (eg is None or eg is False):
            process_attr("eg", eg)
        if not (eh is None or eh is False):
            process_attr("eh", eh)
        if not (ei is None or ei is False):
            process_attr("ei", ei)
        if not (ej is None or ej is False):
            process_attr("ej", ej)
        if not (ek is None or ek is False):
            process_attr("ek", ek)
        if not (el is None or el is False):
            process_attr("el", el)
        if not (em is None or em is False):
            process_attr("em", em)
        if not (en is None or en is False):
            process_attr("en", en)
        if not (eo is None or eo is False):
            process_attr("eo", eo)
        if not (ep is None or ep is False):
            process_attr("ep", ep)
        if not (eq is None or eq is False):
            process_attr("eq", eq)
        if not (er is None or er is False):
            process_attr("er", er)
        if not (es is None or es is False):
            process_attr("es", es)
        if not (et is None or et is False):
            process_attr("et", et)
        if not (eu is None or eu is False):
            process_attr("eu", eu)
        if not (ev is None or ev is False):
            process_attr("ev", ev)
        if not (ew is None or ew is False):
            process_attr("ew", ew)
        if not (ex is None or ex is False):
            process_attr("ex", ex)
        if not (ey is None or ey is False):
            process_attr("ey", ey)
        if not (ez is None or ez is False):
            process_attr("ez", ez)
        if not (fa is None or fa is False):
            process_attr("fa", fa)
        if not (fb is None or fb is False):
            process_attr("fb", fb)
        if not (fc is None or fc is False):
            process_attr("fc", fc)
        if not (fd is None or fd is False):
            process_attr("fd", fd)
        if not (fe is None or fe is False):
            process_attr("fe", fe)
        if not (ff is None or ff is False):
            process_attr("ff", ff)
        if not (fg is None or fg is False):
            process_attr("fg", fg)
        if not (fh is None or fh is False):
            process_attr("fh", fh)
        if not (fi is None or fi is False):
            process_attr("fi", fi)
        if not (fj is None or fj is False):
            process_attr("fj", fj)
        if not (fk is None or fk is False):
            process_attr("fk", fk)
        if not (fl is None or fl is False):
            process_attr("fl", fl)
        if not (fm is None or fm is False):
            process_attr("fm", fm)
        if not (fn is None or fn is False):
            process_attr("fn", fn)
        if not (fo is None or fo is False):
            process_attr("fo", fo)
        if not (fp is None or fp is False):
            process_attr("fp", fp)
        if not (fq is None or fq is False):
            process_attr("fq", fq)
        if not (fr is None or fr is False):
            process_attr("fr", fr)
        if not (fs is None or fs is False):
            process_attr("fs", fs)
        if not (ft is None or ft is False):
            process_attr("ft", ft)
        if not (fu is None or fu is False):
            process_attr("fu", fu)
        if not (fv is None or fv is False):
            process_attr("fv", fv)
        if not (fw is None or fw is False):
            process_attr("fw", fw)
        if not (fx is None or fx is False):
            process_attr("fx", fx)
        if not (fy is None or fy is False):
            process_attr("fy", fy)
        if not (fz is None or fz is False):
            process_attr("fz", fz)
        if not (ga is None or ga is False):
            process_attr("ga", ga)
        if not (gb is None or gb is False):
            process_attr("gb", gb)
        if not (gc is None or gc is False):
            process_attr("gc", gc)
        if not (gd is None or gd is False):
            process_attr("gd", gd)
        if not (ge is None or ge is False):
            process_attr("ge", ge)
        if not (gf is None or gf is False):
            process_attr("gf", gf)
        if not (gg is None or gg is False):
            process_attr("gg", gg)
        if not (gh is None or gh is False):
            process_attr("gh", gh)
        if not (gi is None or gi is False):
            process_attr("gi", gi)
        if not (gj is None or gj is False):
            process_attr("gj", gj)
        if not (gk is None or gk is False):
            process_attr("gk", gk)
        if not (gl is None or gl is False):
            process_attr("gl", gl)
        if not (gm is None or gm is False):
            process_attr("gm", gm)
        if not (gn is None or gn is False):
            process_attr("gn", gn)
        if not (go is None or go is False):
            process_attr("go", go)
        if not (gp is None or gp is False):
            process_attr("gp", gp)
        if not (gq is None or gq is False):
            process_attr("gq", gq)
        if not (gr is None or gr is False):
            process_attr("gr", gr)
        if not (gs is None or gs is False):
            process_attr("gs", gs)
        if not (gt is None or gt is False):
            process_attr("gt", gt)
        if not (gu is None or gu is False):
            process_attr("gu", gu)
        if not (gv is None or gv is False):
            process_attr("gv", gv)
        if not (gw is None or gw is False):
            process_attr("gw", gw)
        if not (gx is None or gx is False):
            process_attr("gx", gx)
        if not (gy is None or gy is False):
            process_attr("gy", gy)
        if not (gz is None or gz is False):
            process_attr("gz", gz)
        if not (ha is None or ha is False):
            process_attr("ha", ha)
        if not (hb is None or hb is False):
            process_attr("hb", hb)
        if not (hc is None or hc is False):
            process_attr("hc", hc)
        if not (hd is None or hd is False):
            process_attr("hd", hd)
        if not (he is None or he is False):
            process_attr("he", he)
        if not (hf is None or hf is False):
            process_attr("hf", hf)
        if not (hg is None or hg is False):
            process_attr("hg", hg)
        if not (hh is None or hh is False):
            process_attr("hh", hh)
        if not (hi is None or hi is False):
            process_attr("hi", hi)
        if not (hj is None or hj is False):
            process_attr("hj", hj)
        if not (hk is None or hk is False):
            process_attr("hk", hk)
        if not (hl is None or hl is False):
            process_attr("hl", hl)
        if not (hm is None or hm is False):
            process_attr("hm", hm)
        if not (hn is None or hn is False):
            process_attr("hn", hn)
        if not (ho is None or ho is False):
            process_attr("ho", ho)
        if not (hp is None or hp is False):
            process_attr("hp", hp)
        if not (hq is None or hq is False):
            process_attr("hq", hq)
        if not (hr is None or hr is False):
            process_attr("hr", hr)
        if not (hs is None or hs is False):
            process_attr("hs", hs)
        if not (ht is None or ht is False):
            process_attr("ht", ht)
        if not (hu is None or hu is False):
            process_attr("hu", hu)
        if not (hv is None or hv is False):
            process_attr("hv", hv)
        if not (hw is None or hw is False):
            process_attr("hw", hw)
        if not (hx is None or hx is False):
            process_attr("hx", hx)
        if not (hy is None or hy is False):
            process_attr("hy", hy)
        if not (hz is None or hz is False):
            process_attr("hz", hz)
        if not (ia is None or ia is False):
            process_attr("ia", ia)
        if not (ib is None or ib is False):
            process_attr("ib", ib)
        if not (ic is None or ic is False):
            process_attr("ic", ic)
        if not (id is None or id is False):
            process_attr("id", id)
        if not (ie is None or ie is False):
            process_attr("ie", ie)
        if not (if_ is None or if_ is False):
            process_attr("if_", if_)
        if not (ig is None or ig is False):
            process_attr("ig", ig)
        if not (ih is None or ih is False):
            process_attr("ih", ih)
        if not (ii is None or ii is False):
            process_attr("ii", ii)
        if not (ij is None or ij is False):
            process_attr("ij", ij)
        if not (ik is None or ik is False):
            process_attr("ik", ik)
        if not (il is None or il is False):
            process_attr("il", il)
        if not (im is None or im is False):
            process_attr("im", im)
        if not (in_ is None or in_ is False):
            process_attr("in_", in_)
        if not (io is None or io is False):
            process_attr("io", io)

    def control_func(
        aa=None,
        ab=None,
        ac=None,
        ad=None,
        ae=None,
        af=None,
        ag=None,
        ah=None,
        ai=None,
        aj=None,
        ak=None,
        al=None,
        am=None,
        an=None,
        ao=None,
        ap=None,
        aq=None,
        ar=None,
        at=None,
        au=None,
        av=None,
        aw=None,
        ax=None,
        ay=None,
        az=None,
        ba=None,
        bb=None,
        bc=None,
        bd=None,
        be=None,
        bf=None,
        bg=None,
        bh=None,
        bi=None,
        bj=None,
        bk=None,
        bl=None,
        bm=None,
        bn=None,
        bo=None,
        bp=None,
        bq=None,
        br=None,
        bs=None,
        bt=None,
        bu=None,
        bv=None,
        bw=None,
        bx=None,
        by=None,
        bz=None,
        ca=None,
        cb=None,
        cc=None,
        cd=None,
        ce=None,
        cf=None,
        cg=None,
        ch=None,
        ci=None,
        cj=None,
        ck=None,
        cl=None,
        cm=None,
        cn=None,
        co=None,
        cp=None,
        cq=None,
        cr=None,
        cs=None,
        ct=None,
        cu=None,
        cv=None,
        cw=None,
        cx=None,
        cy=None,
        cz=None,
        da=None,
        db=None,
        dc=None,
        dd=None,
        de=None,
        df=None,
        dg=None,
        dh=None,
        di=None,
        dj=None,
        dk=None,
        dl=None,
        dm=None,
        dn=None,
        do=None,
        dp=None,
        dq=None,
        dr=None,
        ds=None,
        dt=None,
        du=None,
        dv=None,
        dw=None,
        dx=None,
        dy=None,
        dz=None,
        ea=None,
        eb=None,
        ec=None,
        ed=None,
        ee=None,
        ef=None,
        eg=None,
        eh=None,
        ei=None,
        ej=None,
        ek=None,
        el=None,
        em=None,
        en=None,
        eo=None,
        ep=None,
        eq=None,
        er=None,
        es=None,
        et=None,
        eu=None,
        ev=None,
        ew=None,
        ex=None,
        ey=None,
        ez=None,
        fa=None,
        fb=None,
        fc=None,
        fd=None,
        fe=None,
        ff=None,
        fg=None,
        fh=None,
        fi=None,
        fj=None,
        fk=None,
        fl=None,
        fm=None,
        fn=None,
        fo=None,
        fp=None,
        fq=None,
        fr=None,
        fs=None,
        ft=None,
        fu=None,
        fv=None,
        fw=None,
        fx=None,
        fy=None,
        fz=None,
        ga=None,
        gb=None,
        gc=None,
        gd=None,
        ge=None,
        gf=None,
        gg=None,
        gh=None,
        gi=None,
        gj=None,
        gk=None,
        gl=None,
        gm=None,
        gn=None,
        go=None,
        gp=None,
        gq=None,
        gr=None,
        gs=None,
        gt=None,
        gu=None,
        gv=None,
        gw=None,
        gx=None,
        gy=None,
        gz=None,
        ha=None,
        hb=None,
        hc=None,
        hd=None,
        he=None,
        hf=None,
        hg=None,
        hh=None,
        hi=None,
        hj=None,
        hk=None,
        hl=None,
        hm=None,
        hn=None,
        ho=None,
        hp=None,
        hq=None,
        hr=None,
        hs=None,
        ht=None,
        hu=None,
        hv=None,
        hw=None,
        hx=None,
        hy=None,
        hz=None,
        ia=None,
        ib=None,
        ic=None,
        id=None,
        ie=None,
        if_=None,
        ig=None,
        ih=None,
        ii=None,
        ij=None,
        ik=None,
        il=None,
        im=None,
        in_=None,
        io=None,
    ):
        pass

    RUN_NUM = 70000
    dstart = perf_counter()
    for i in range(RUN_NUM):
        fn1(
            aa="https://example.com",
            ab="https://example.com",
            ac="https://example.com",
            ad="https://example.com",
            ae="https://example.com",
            af="https://example.com",
            ag="https://example.com",
            ah="https://example.com",
            ai="https://example.com",
            aj="https://example.com",
            ak="https://example.com",
            al="https://example.com",
            am="https://example.com",
            an="https://example.com",
            ao="https://example.com",
            ap="https://example.com",
            aq="https://example.com",
            ar="https://example.com",
            at="https://example.com",
            au="https://example.com",
            av="https://example.com",
            aw="https://example.com",
            ax="https://example.com",
            ay="https://example.com",
            az="https://example.com",
            ba="https://example.com",
            bb="https://example.com",
            bc="https://example.com",
            bd="https://example.com",
            be="https://example.com",
            bf="https://example.com",
        )
    dend = perf_counter()

    d2start = perf_counter()
    for i in range(RUN_NUM):
        fn2(
            aa="https://example.com",
            ab="https://example.com",
            ac="https://example.com",
            ad="https://example.com",
            ae="https://example.com",
            af="https://example.com",
            ag="https://example.com",
            ah="https://example.com",
            ai="https://example.com",
            aj="https://example.com",
            ak="https://example.com",
            al="https://example.com",
            am="https://example.com",
            an="https://example.com",
            ao="https://example.com",
            ap="https://example.com",
            aq="https://example.com",
            ar="https://example.com",
            at="https://example.com",
            au="https://example.com",
            av="https://example.com",
            aw="https://example.com",
            ax="https://example.com",
            ay="https://example.com",
            az="https://example.com",
            ba="https://example.com",
            bb="https://example.com",
            bc="https://example.com",
            bd="https://example.com",
            be="https://example.com",
            bf="https://example.com",
        )

    d2end = perf_counter()

    d3start = perf_counter()
    for i in range(RUN_NUM):
        control_func(
            aa="https://example.com",
            ab="https://example.com",
            ac="https://example.com",
            ad="https://example.com",
            ae="https://example.com",
            af="https://example.com",
            ag="https://example.com",
            ah="https://example.com",
            ai="https://example.com",
            aj="https://example.com",
            ak="https://example.com",
            al="https://example.com",
            am="https://example.com",
            an="https://example.com",
            ao="https://example.com",
            ap="https://example.com",
            aq="https://example.com",
            ar="https://example.com",
            at="https://example.com",
            au="https://example.com",
            av="https://example.com",
            aw="https://example.com",
            ax="https://example.com",
            ay="https://example.com",
            az="https://example.com",
            ba="https://example.com",
            bb="https://example.com",
            bc="https://example.com",
            bd="https://example.com",
            be="https://example.com",
            bf="https://example.com",
        )

    d3end = perf_counter()
    test1_delta = dend - dstart
    test2_delta = d2end - d2start
    test3_delta = d3end - d3start
    print(f"Test 1: {test1_delta} seconds")
    print(f"Test 2: {test2_delta} seconds")
    print(f"Test 3: {test3_delta} seconds")

    # Ensure that test 1 (arg unpacking isn't
    # more than 50% slower than test 2 (kwargs unpacking)
    assert test1_delta <= test2_delta * 1.50, (
        "Test 1 should not be more than 50% slower than Test 2"
    )
    # Verify that the control function is at least 50% faster than test 1
    # If this varies, just increase the factor but we're trying to use this
    # to confirm we understand the percentage of time we're measuring
    assert test3_delta < test1_delta * 0.5, (
        "Control function should be at least 50% faster than Test 1"
    )
