
/********************************************************************
  ngRoute
*********************************************************************/

var mainApp = angular.module("salesCRM", ['ngMessages', 'ngRoute', 'ngCookies', 'ngResource', 'ngAnimate', 'ngAria']);

mainApp.config(['$routeProvider', function($routeProvider) {
     
    $routeProvider.
    
    when('/deals/list', {
        templateUrl: 'pages/deals/list.html'
    }).
    when('/deals/grid', {
        templateUrl: 'pages/deals/grid.html'
    }).
    when('/deals/view', {
        templateUrl: 'pages/deals/view.html',
        className: 'bg-grey'   // <--- class name
    }).
    
    otherwise({
        templateUrl: 'pages/deals/list.html'
    });
}]);

mainApp.controller('mainController', function($scope, $route, $location) {
    $scope.$on('$routeChangeSuccess', function(newVal, oldVal) {
        if (oldVal !== newVal) {
            $scope.routeClassName = $route.current.className;
        }
    })
});
