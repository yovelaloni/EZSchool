#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Dec 19, 2020 05:21:25 PM +0200  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+662+274
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "zoom links for student"
    vTcl:DefineAlias "$top" "zoom links teacher" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -cursor hand2 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור מתמטיקה} 
    vTcl:DefineAlias "$top.but45" "zoom_math" vTcl:WidgetProc "zoom links teacher" 1
    menu $top.m46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -cursor hand2 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור היסטוריה} 
    vTcl:DefineAlias "$top.but47" "zoom_history" vTcl:WidgetProc "zoom links teacher" 1
    button $top.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -cursor hand2 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור תנך} 
    vTcl:DefineAlias "$top.but48" "zoom_bible" vTcl:WidgetProc "zoom links teacher" 1
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -cursor hand2 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור לשיעור עברית} 
    vTcl:DefineAlias "$top.but49" "zoom_hebrew" vTcl:WidgetProc "zoom links teacher" 1
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -cursor hand2 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {קישור מעודכן מהמורה} 
    vTcl:DefineAlias "$top.but46" "zoom_updated_link" vTcl:WidgetProc "zoom links teacher" 1
    label $top.lab47 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -text {אם המורה ביקש להיכנס דרך קישור מעודכן אנא לחצו כאן} 
    vTcl:DefineAlias "$top.lab47" "zoom_label" vTcl:WidgetProc "zoom links teacher" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but45 \
        -in $top -x 0 -relx 0.25 -y 0 -rely 0.022 -width 296 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.25 -y 0 -rely 0.2 -width 296 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 0 -relx 0.25 -y 0 -rely 0.378 -width 296 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.25 -y 0 -rely 0.556 -width 296 -relwidth 0 \
        -height 63 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 0 -relx 0.25 -y 0 -rely 0.8 -width 306 -relwidth 0 \
        -height 83 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.283 -y 0 -rely 0.733 -width 0 -relwidth 0.703 \
        -height 0 -relheight 0.058 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

