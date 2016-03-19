def remove_url(article):
    def regex_or(*items):
        r = '|'.join(items)
        r = '(' + r + ')'
        return r

    def pos_lookahead(r):
        return '(?=' + r + ')'

    def neg_lookahead(r):
        return '(?!' + r + ')'

    def optional(r):
        return '(%s)?' % r

    PunctChars = r'''['".?!,:;]'''
    Punct = '%s+' % PunctChars
    Entity = '&(amp|lt|gt|quot);'

    UrlStart1 = regex_or(r'https?://?', r'www\.')
    CommonTLDs = regex_or('com', 'co\\.uk', 'org', 'net', 'info', 'ca')
    UrlStart2 = r'[a-z0-9\.-]+?' + r'\.' + CommonTLDs + pos_lookahead(r'[/ \W\b]')
    UrlBody = r'[^ \t\r\n<>]*?'
    UrlExtraCrapBeforeEnd = '%s+?' % regex_or(PunctChars, Entity)
    UrlEnd = regex_or(r'\.\.+', r'[<>]', r'\s', '$')
    Url = (r'\b' +
           regex_or(UrlStart1, UrlStart2) +
           UrlBody +
           pos_lookahead(optional(UrlExtraCrapBeforeEnd) + UrlEnd))

    Url_RE = re.compile("(%s)" % Url, re.U | re.I)
    article = re.sub(Url_RE, "", article)

    return article