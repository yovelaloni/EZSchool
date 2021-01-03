#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#  Dec 31, 2020 03:09:14 PM +0200  platform: Windows NT
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
set vTcl(mode) Absolute
}



    menu .pop51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop51" "Popupmenu1" vTcl:WidgetProc "" 1

proc vTclWindow.top60 {base} {
    global vTcl
    if {$base == ""} {
        set base .top60
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #d9ffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x443+385+120
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1540 845
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "מערכת שעות כיתה ד"
    vTcl:DefineAlias "$top" "classes_Sche3" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but67 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #00eaea -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {חזרה לכיתות} 
    vTcl:DefineAlias "$top.but67" "back" vTcl:WidgetProc "classes_Sche3" 1
    message $top.mes68 \
        -background #d9ffff \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {מערכת שעות כיתה ד} -width 310 
    vTcl:DefineAlias "$top.mes68" "Message1" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but55" "sunday1" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but56" "sunday2" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but57" "sunday5" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but58" "sunday3" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but59" "monday1" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but60" "tuesday1" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but61" "sunday4" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but61.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but61.but62" "Button8" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but63 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but63" "wednesday1" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but64 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but64" "thursday1" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but65 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but65" "monday2" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but66 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but66" "monday3" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but68 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but68" "monday4" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but69 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but69" "monday5" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but70 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but70" "tuesday2" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but71 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but71" "tuesday3" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but74 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but74" "tuesday4" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but75 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but75" "tuesday5" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but76 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but76" "wednesday2" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but77 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but77" "wednesday3" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but78 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but78" "wednesday4" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but79 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but79" "wednesday5" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but80 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but80" "thursday2" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but81 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but81" "thursday3" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but82 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but82" "thursday4" vTcl:WidgetProc "classes_Sche3" 1
    button $top.but83 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #a6ffff -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but83" "thursday5" vTcl:WidgetProc "classes_Sche3" 1
    message $top.mes84 \
        -background #d9ffff \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text ראשון -width 60 
    vTcl:DefineAlias "$top.mes84" "day1" vTcl:WidgetProc "classes_Sche3" 1
    message $top.mes85 \
        -background #d9ffff \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text שני -width 60 
    vTcl:DefineAlias "$top.mes85" "day2" vTcl:WidgetProc "classes_Sche3" 1
    message $top.mes86 \
        -background #d9ffff \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text שלישי -width 60 
    vTcl:DefineAlias "$top.mes86" "day3" vTcl:WidgetProc "classes_Sche3" 1
    message $top.mes87 \
        -background #d9ffff \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text רביעי -width 60 
    vTcl:DefineAlias "$top.mes87" "day4" vTcl:WidgetProc "classes_Sche3" 1
    message $top.mes88 \
        -background #d9ffff \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text חמישי -width 60 
    vTcl:DefineAlias "$top.mes88" "day5" vTcl:WidgetProc "classes_Sche3" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but67 \
        -in $top -x 0 -relx 0.067 -y 0 -rely 0.867 -width 117 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.mes68 \
        -in $top -x 140 -y 20 -width 0 -relwidth 0.517 -height 0 \
        -relheight 0.073 -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 450 -y 90 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but56 \
        -in $top -x 450 -y 140 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but57 \
        -in $top -x 450 -y 290 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but58 \
        -in $top -x 450 -y 190 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but59 \
        -in $top -x 330 -y 90 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but60 \
        -in $top -x 230 -y 90 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but61 \
        -in $top -x 450 -y 240 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but61.but62 \
        -in $top.but61 -x -90 -y 50 -anchor nw -bordermode ignore 
    place $top.but63 \
        -in $top -x 120 -y 90 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but64 \
        -in $top -x 20 -y 90 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but65 \
        -in $top -x 330 -y 140 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but66 \
        -in $top -x 330 -y 190 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but68 \
        -in $top -x 330 -y 240 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but69 \
        -in $top -x 330 -y 290 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but70 \
        -in $top -x 230 -y 140 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but71 \
        -in $top -x 230 -y 190 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but74 \
        -in $top -x 230 -y 240 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but75 \
        -in $top -x 230 -y 290 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but76 \
        -in $top -x 120 -y 140 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but77 \
        -in $top -x 120 -y 190 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but78 \
        -in $top -x 120 -y 240 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but79 \
        -in $top -x 120 -y 290 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but80 \
        -in $top -x 20 -y 140 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but81 \
        -in $top -x 20 -y 190 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but82 \
        -in $top -x 20 -y 240 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but83 \
        -in $top -x 20 -y 290 -width 77 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes84 \
        -in $top -x 460 -y 60 -anchor nw -bordermode ignore 
    place $top.mes85 \
        -in $top -x 350 -y 60 -anchor nw -bordermode ignore 
    place $top.mes86 \
        -in $top -x 240 -y 60 -anchor nw -bordermode ignore 
    place $top.mes87 \
        -in $top -x 130 -y 60 -anchor nw -bordermode ignore 
    place $top.mes88 \
        -in $top -x 30 -y 60 -anchor nw -bordermode ignore 
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
Window show .top60 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

