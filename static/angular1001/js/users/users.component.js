'use strict';
//Create service with help of factory
mainApp.factory("User", ['$http', function($http) {
    var obj = {};

    obj.getUserList = function(page = null) {
        var req = {
            method: 'GET',
            url: '/api/v1/user/',
            params: {
                page: page,
            }
        }
        return $http(req);
    }


    obj.addUser = function(data) {
        var req = {
            method: 'POST',
            url: '/api/v1/user/',
            data: data,
        }
        return $http(req);
    }

    obj.getUserDetail = function(data) {
        var req = {
            method: 'GET',
            url: '/api/v1/user/',
            params: {
                id: data,
            },
        }
        return $http(req);
    }

    obj.updateUser = function(data) {
        var req = {
            method: 'PUT',
            url: '/api/v1/user/',
            data: data,
        }
        return $http(req);
    }

    return obj;
}]);


//Create User Component Defination
userApp.
component('users', {
    templateUrl: 'djangotemplates/front/users/list.html',
    controller: function(
        $http,
        $location,
        $rootScope,
        $scope,
        User,
        Flash,
        $mdToast
    ) {

        //Get User List
        User.getUserList().success(function(response) {
            $scope.total = response.total;
            $scope.has_next = response.has_next;
            $scope.has_previous = response.has_previous;
            $scope.previous_page_number = response.previous_page_number;
            $scope.pages = response.pages;
            $scope.next_page_number = response.next_page_number;
            $scope.usersData = response.User;
        }).error(function(e_data, e_status, e_headers, e_config) {});


        //Edit Button Action
        $scope.editClicked = function(user) {
            $scope.user = user;
            User.getUserDetail(user.id).success(function(response) {
                if (response.User && response.User[0]) {
                    $scope.user = response.User[0];
                }
            }).error(function(e_data, e_status, e_headers, e_config) {});


        }

        //Add User Api/Service Calling
        $scope.doAddUser = function(user, valid) {
            var fd = new FormData();
            fd.append('file', $scope.myFile);
            for (var key in user)
                fd.append(key, user[key]);
            if (valid) {
                if (!user.id) {
                    User.addUser(user).success(function(response) {
                        $('#myModal').modal('toggle');
                        $mdToast.show({
                            template: '<md-toast class="md-toast">' + "New User Added" + '</md-toast>',
                            hideDelay: 6000,
                            position: 'bottom left'
                        });
                        if (response.User)
                            response.User.new = true
                        $scope.usersData.splice(0, 0, response.User);

                    }).error(function(e_data, e_status, e_headers, e_config) {

                        $mdToast.show(
                            $mdToast.simple()
                            .textContent(e_data.message)
                            .position("bottom left")
                            .hideDelay(3000)
                        );

                    });
                } else {
                    //Update User Api/Service Calling
                    User.updateUser(user).success(function(response) {
                        $('#myModal').modal('toggle');
                        $mdToast.show({
                            template: '<md-toast class="md-toast">' + "User Updated Successfully " + '</md-toast>',
                            hideDelay: 6000,
                            position: 'bottom left'
                        });
                        User.getUserList().success(function(response) {
                            $scope.total = response.total;
                            $scope.has_next = response.has_next;
                            $scope.has_previous = response.has_previous;
                            $scope.previous_page_number = response.previous_page_number;
                            $scope.pages = response.pages;
                            $scope.next_page_number = response.next_page_number;
                            $scope.usersData = response.User;
                        }).error(function(e_data, e_status, e_headers, e_config) {
                        });
                    }).error(function(e_data, e_status, e_headers, e_config) {
                        var type = "error"

                        $mdToast.show({
                            template: '<md-toast class="md-toast ' + type + '">' + e_data.message + '</md-toast>',
                            hideDelay: 6000,
                            position: 'top center'
                        });
                    });
                }

            }
        }


        //Load more Broad Cast
        $scope.$on("loadMoreUsers", function(ev) {

            if ($scope.has_next && !$scope.loadMore) {

                $scope.loadMore = true;

                setTimeout(function() {
                    User.getUserList($scope.next_page_number).success(function(response) {
                        $scope.loadMore = false;
                        $scope.total = response.total;
                        $scope.has_next = response.has_next;
                        $scope.has_previous = response.has_previous;
                        $scope.previous_page_number = response.previous_page_number;
                        $scope.pages = response.pages;
                        $scope.next_page_number = response.next_page_number;
                        $scope.usersData = $scope.usersData.concat(response.User);
                    }).error(function(e_data, e_status, e_headers, e_config) {
                        $scope.loadMore = false;
                    });
                }, 1000);



            }


        })

        //Delete Action
        $scope.deletUser = function(user, index) {

            var res = confirm("User " + user.first_name + "will be Permenenty delete form the list?");
            if (res) {
                user.is_deleted = true;
                User.updateUser(user).success(function(response) {
                    if (response.code == 200) {
                        $scope.usersData.splice(index, 1);

                        $mdToast.show({
                            template: '<md-toast class="md-toast">' + "User Deleted Successfully " + '</md-toast>',
                            hideDelay: 6000,
                            position: 'bottom left'
                        });

                    }

                }).error(function(e_data, e_status, e_headers, e_config) {
                    Flash.create("error", e_data.message, 0);
                });
            }

        }


    }
})

//load more Directives
mainApp.directive('scroll', function() {

    return {

        restrict: 'A',
        link: function(rootScope, element, attrs, $window, $scope, $rootScope, $document) {
            var bind = element.bind('div');
            var raw = element[0];
            angular.element(bind).on("scroll", function() {
                if (raw.scrollTop + raw.offsetHeight >= raw.scrollHeight) {
                    rootScope.$broadcast("loadMoreUsers")
                }
            });
        }
    };
});