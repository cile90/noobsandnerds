#! /usr/bin/python

def get_string(t):
    from meta import plugin
    id = _ALL.get(t.lower())
    if id:
        return plugin.get_string(id)
    else:
        plugin.log.error("missing translation for " + t.lower())
        return t
_ALL = {}

if __name__ == "__main__":
    import polib
    po = polib.pofile('resources/language/English/strings.po')
    try:
        import re
        import subprocess
        r = subprocess.check_output(["grep", "-hnr", "_([\'\"]", "."])
        strings = re.compile("_\([\"'](.*?)[\"']\)", re.IGNORECASE).findall(r)
        translated = [m.msgid.lower().replace("'", "\\'") for m in po]
        missing = set([s for s in strings if s.lower() not in translated])
        if missing:
            ids_range = range(30000, 31000)
            ids_reserved = [int(m.msgctxt[1:]) for m in po]
            ids_available = [x for x in ids_range if x not in ids_reserved]
            print "warning: missing translation for", missing
            for text in missing:
                id = ids_available.pop(0)
                entry = polib.POEntry(msgid=text, msgstr=u'', msgctxt="#{0}".format(id))
                po.append(entry)
            po.save('resources/language/English/strings.po')
    except:
        pass
    content = []
    with open(__file__, "r") as me:
        content = me.readlines()
        content = content[:content.index("#GENERATED\n")+1]
    with open(__file__, 'w') as f:
        f.writelines(content)
        for m in po:
            line = "_ALL['{0}'] = {1}\n".format(m.msgid.lower().replace("'", "\\'"), m.msgctxt.replace('#', '').strip())
            f.write(line)

#GENERATED
_ALL['general'] = 30000
_ALL['move down'] = 30001
_ALL['move up'] = 30002
_ALL['clear channels'] = 30003
_ALL['remove channel'] = 30004
_ALL['style'] = 30005
_ALL['select stream...'] = 30006
_ALL['add to list'] = 30007
_ALL['channel'] = 30008
_ALL['channels'] = 30009
_ALL['players url'] = 30010
_ALL['install from url'] = 30012
_ALL['cache deleted'] = 30013
_ALL['failed to delete cache'] = 30014
_ALL['background'] = 30015
_ALL['custom style folder'] = 30016
_ALL['custom background folder'] = 30017
_ALL['my channels'] = 30020
_ALL['new channel'] = 30021
_ALL['all movie players'] = 30030
_ALL['all tv show players'] = 30031
_ALL['all musicvideo players'] = 30032
_ALL['all music players'] = 30033
_ALL['all live players'] = 30034
_ALL['all players'] = 30035
_ALL['enabled'] = 30036
_ALL['automated install'] = 30037
_ALL['started'] = 30038
_ALL['players'] = 30039
_ALL['updated'] = 30040
_ALL['movies library folder'] = 30041
_ALL['tv shows library folder'] = 30042
_ALL['music library folder'] = 30043
_ALL['live library folder'] = 30044
_ALL['setup done'] = 30045
_ALL['completed'] = 30046
_ALL['movies'] = 30100
_ALL['enable movie players'] = 30101
_ALL['preferred movie player'] = 30110
_ALL['preferred movie player from library'] = 30111
_ALL['preferred movie player from context menu'] = 30112
_ALL['would you like to automatically set [color ff0084ff]m[/color]etalli[color ff0084ff]q[/color] as a movie video source?'] = 30113
_ALL['movie trailer'] = 30114
_ALL['recommended movies (tmdb)'] = 30115
_ALL['tv shows'] = 30200
_ALL['enable tv show players'] = 30201
_ALL['preferred tv show player'] = 30210
_ALL['preferred tv show player from library'] = 30211
_ALL['preferred tv show player from context menu'] = 30212
_ALL['would you like to automatically set [color ff0084ff]m[/color]etalli[color ff0084ff]q[/color] as a tv shows video source?'] = 30213
_ALL['tv trailer'] = 30214
_ALL['recommended tv shows (tmdb)'] = 30215
_ALL['library'] = 30300
_ALL['library folder'] = 30301
_ALL['library folder'] = 30302
_ALL['update libraries'] = 30303
_ALL['advanced'] = 30400
_ALL['clear cache'] = 30401
_ALL['automatic movies library server'] = 30304
_ALL['enable library updates'] = 30306
_ALL['movies library updates enabled'] = 30307
_ALL['tv shows library updates enabled'] = 30308
_ALL['music library updates enabled'] = 30309
_ALL['use simple selection dialog'] = 30402
_ALL['number of simultaneous searches'] = 30404
_ALL['attempt to hide dialogs while [color ff0084ff]m[/color]etalli[color ff0084ff]q[/color] is searching'] = 30410
_ALL['hide progress dialogs'] = 30411
_ALL['hide information dialogs'] = 30412
_ALL['hide keyboard dialog'] = 30413
_ALL['watchlist'] = 30414
_ALL['please go to https://trakt.tv/activate and enter the code'] = 30415
_ALL['next episodes'] = 30416
_ALL['authenticate trakt'] = 30417
_ALL['add all to library'] = 30418
_ALL['are you sure you want to add your entire trakt collection to kodi library?'] = 30419
_ALL['collection'] = 30420
_ALL['are you sure you want to add your entire trakt watchlist to kodi library?'] = 30421
_ALL['you must authenticate with trakt. do you want to authenticate now?'] = 30422
_ALL['calendar'] = 30423
_ALL['recommendations'] = 30424
_ALL['live'] = 30500
_ALL['enable live players'] = 30501
_ALL['preferred live player'] = 30510
_ALL['preferred live player from library'] = 30511
_ALL['preferred live player from context menu'] = 30512
_ALL['would you like to automatically set [color ff0084ff]m[/color]etalli[color ff0084ff]q[/color] as a channel video source?'] = 30513
_ALL['genres (tmdb)'] = 30601
_ALL['select default player'] = 30602
_ALL['show info'] = 30603
_ALL['video not found :('] = 30604
_ALL['add to library'] = 30605
_ALL['do you want to remove your existing players first?'] = 30606
_ALL['enter password'] = 30607
_ALL['players updated'] = 30608
_ALL['enable players'] = 30609
_ALL['season'] = 30610
_ALL['top rated (tmdb)'] = 30612
_ALL['blockbusters (tmdb)'] = 30613
_ALL['on the air (tmdb)'] = 30614
_ALL['update players'] = 30615
_ALL['search'] = 30617
_ALL['search for'] = 30618
_ALL['next >>'] = 30619
_ALL['error'] = 30620
_ALL['popular (tmdb)'] = 30621
_ALL['context player'] = 30622
_ALL['failed to update players'] = 30623
_ALL['in theatres (tmdb)'] = 30624
_ALL['select player'] = 30625
_ALL['warning'] = 30626
_ALL['library setup'] = 30627
_ALL['play with...'] = 30628
_ALL['trending (trakt)'] = 30629
_ALL['personal (trakt)'] = 30630
_ALL['aired (trakt)'] = 30631
_ALL['premiered (trakt)'] = 30632
_ALL['search (tmdb)'] = 30633
_ALL['search artist'] = 30634
_ALL['search album'] = 30635
_ALL['search track'] = 30636
_ALL['search list'] = 30637
_ALL['search (trakt)'] = 30638
_ALL['next page'] = 30639
_ALL['preferred music type'] = 30699
_ALL['musicvideos'] = 30700
_ALL['enable musicvideos players'] = 30701
_ALL['musicvideo'] = 30702
_ALL['preferred musicvideo player'] = 30710
_ALL['preferred musicvideo player from library'] = 30711
_ALL['preferred musicvideo player from context menu'] = 30712
_ALL['would you like to automatically set [color ff0084ff]m[/color]etalli[color ff0084ff]q[/color] as a musicvideo video source?'] = 30713
_ALL['personal (trakt)'] = 30714
_ALL['popular (trakt)'] = 30715
_ALL['most played (trakt)'] = 30716
_ALL['most watched (trakt)'] = 30717
_ALL['most collected (trakt)'] = 30718
_ALL['related movies (trakt)'] = 30719
_ALL['period to use for most-sections (trakt)'] = 30720
_ALL['items per page (trakt)'] = 30721
_ALL['number of days to use for recently updated-section (trakt)'] = 30722
_ALL['recently updated (trakt)'] = 30723
_ALL['music'] = 30800
_ALL['enable music players'] = 30801
_ALL['library folder'] = 30802
_ALL['top artists'] = 30803
_ALL['top tracks'] = 30804
_ALL['preferred music player'] = 30810
_ALL['preferred music player from library'] = 30811
_ALL['preferred music player from context menu'] = 30812
_ALL['would you like to automatically set [color ff0084ff]m[/color]etalli[color ff0084ff]q[/color] as a music video source?'] = 30813
_ALL['[color ff0084ff]q[/color]lick[color ff0084ff]p[/color]lay'] = 30814
_ALL['lists'] = 30815
_ALL['liked lists'] = 30816
_ALL['my lists'] = 30817
_ALL['add tv shows to library using preferred library player?'] = 30818
_ALL['choose movie'] = 30819
_ALL['add movies played by name to library automaticly?'] = 30820
_ALL['add tv shows played by name to library automaticly?'] = 30821
_ALL['meta'] = 30822
_ALL['adding music to database'] = 30823
_ALL['enable library updates'] = 30824
_ALL['appearance'] = 30825
_ALL['views'] = 30826
_ALL['language for tmdb'] = 30827
_ALL['force views'] = 30828
_ALL['extended movie info'] = 30829
_ALL['extended tv show info'] = 30830
_ALL['play by name'] = 30831
_ALL['play by name only'] = 30832
_ALL['[color ff0084ff]m[/color]etalli[color ff0084ff]q[/color]'] = 30833
_ALL['add movies to library using preferred library player?'] = 30834