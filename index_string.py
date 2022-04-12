index_str='''
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="au theme template">
    <meta name="author" content="Hau Nguyen">
    <meta name="keywords" content="au theme template">
    <link rel=icon href= '../../static/system_dashboard/images/icon/Dsa_icon.png' sizes="32x32" type="image/png">

    <!-- Title Page-->
    <title>DASHBOARD</title>

    <!-- Fontfaces CSS-->
    <link href="../../static/system_dashboard/css/font-face.css" rel="stylesheet" media="all">
    <link href="../../static/system_dashboard/vendor/font-awesome-5/css/fontawesome-all.min.css" rel="stylesheet" media="all">

    <!-- Bootstrap CSS-->
    <link href="../../static/system_dashboard/vendor/bootstrap-4.1/bootstrap.min.css" rel="stylesheet" media="all">

    <!-- Vendor CSS-->
    <link href="../../static/system_dashboard/vendor/animsition/animsition.min.css" rel="stylesheet" media="all">

    <!-- Main CSS-->
    <link rel="stylesheet" href="../../static/system_dashboard/css/OverlayScrollbars.min.css" media="all">
    <link rel="stylesheet" href="../../static/system_dashboard/css/adminlte.min.css" >
    <link href="../../static/system_dashboard/css/theme.css" rel="stylesheet" media="all">
    <link href="../../static/system_dashboard/css/style.css" rel="stylesheet">
</head>

<body class="animsition sidebar-mini layout-fixed sidebar-collapse">
    <div class="page-wrapper">
        <!-- MENU SIDEBAR-->
        <aside class="main-sidebar sidebar-dark-primary elevation-4" id="menu_dsa" w="73">
            <div class="logo">
                <a href="#" class="brand-link text-center">
                    <img class="icon brand-image img-circle logo-dsa" id="logo_dsa" src="../../static/system_dashboard/images/icon/Dsa_icon.png" alt="DSA COMPANY" />
                </a>
            </div>
            <div class="sidebar">
                <nav class="mt-2 navbar-sidebar2">
                    <ul id="menu_item" class="nav nav-pills nav-sidebar flex-column navbar__list" data-widget="treeview" role="menu" data-accordion="false">
                      <li class="nav-item">
                        <a id='home' href="/" class="nav-link js-arrow">
                          <i class="nav-icon fad fa-home-lg"></i>
                          <p>Trang chủ</p>
                        </a>
                      </li>
                    </ul>
                  </nav>
            </div>
        </aside>
        <!-- END MENU SIDEBAR-->

        <!-- HEADER DESKTOP-->
        <header class="header-desktop main-header" style="z-index: 999;">
            <div class="section__content section__content--p30">
                <div class="container-fluid">
                    <div class="header-wrap">
                        
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link" data-widget="pushmenu" href="#" role="button" id="click_menu"><i class="fa-icon fas fa-bars"></i></a>
                            </li>
                        </ul>

                        <div class="header-button" style="justify-content: end;">
                            <a href="/logout" class="btn btn-success"><i class="fa fa-power-off" aria-hidden="true"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </header>

        <!-- HEADER DESKTOP-->

        <!-- PAGE CONTAINER-->
        <div class="content-wrapper" style='width:auto; height:100%'>

            <!-- MAIN CONTENT-->
            <div class="main-content" style='width:100%; height:100%'>
                {%app_entry%}
            </div>
            <!-- END MAIN CONTENT-->

        </div>
        <!-- END PAGE CONTAINER-->
    </div>

    <footer>
        {%config%}
        {%scripts%}
        {%renderer%}
    </footer>

    <!-- Jquery JS-->
    <script src="../../static/system_dashboard/vendor/jquery-3.2.1.min.js"></script>
    
    <!-- Vendor JS-->
    <script src="../../static/system_dashboard/vendor/animsition/animsition.min.js"></script></script>

    <!-- Main JS-->
    <script src="../../static/system_dashboard/js/adminlte.js"></script>
    <script src="../../static/system_dashboard/js/main.js"></script>

    <script src="../../static/system_dashboard/js/custom_dash.js"></script>
    <script src="../../static/system_dashboard/js/all.js"></script>
</body>

</html>
'''